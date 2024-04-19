from botcity.core import DesktopBot


# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the Spotify website.
        self.browse("https://open.spotify.com/intl-pt")
        self.browse("https://www.bing.com/")

        # Opens E-tree
        if self.find( "e-tree", matching=0.97, waiting_time=30000):
            self.click()

            # Collect the daily water
            if self.find( "first_collection", matching=0.97, waiting_time=30000):
                self.click()
            else:
                self.not_found("first_collection")

            # Opens the reward page
            if self.find( "rewardPage", matching=0.97, waiting_time=10000):
                self.click()

                # Check if Wallet mission exists
                if self.find( "walletMission", matching=0.97, waiting_time=10000):
                    self.click()
                    if self.find( "walletGo", matching=0.97, waiting_time=10000):
                        self.click()
                        self.wait(5000)
                        self.control_w()
                    else:
                        self.not_found("walletGo")
                else:
                    self.not_found("walletMission")

                # Check if the Office mission exists
                if self.find( "officeMission", matching=0.97, waiting_time=10000):
                    self.click()
                    if self.find( "officeGo", matching=0.97, waiting_time=10000):
                        self.click()
                        self.wait(5000)
                        self.control_w()
                    else:
                        self.not_found("officeGo")
                else:
                    self.not_found("officeMission")

                # Opens the rewards
                if self.find( "ambiente", matching=0.97, waiting_time=10000):
                    self.click()
                    if self.find( "go", matching=0.97, waiting_time=10000):
                        self.click()
                        self.wait(5000)
                        self.click_at(x=600, y=300)
                        self.wait(10000)
                        self.key_f9()
                        self.wait(5000)
                        if self.find( "ctrlShiftU", matching=0.97, waiting_time=10000):
                            self.click()
                        else:
                            self.not_found("ctrlShiftU")
                        self.wait(15000)
                        self.control_w()
                        self.control_w()
                    else:
                        self.not_found("go")
                else:
                    self.not_found("ambiente")

                # Check if there is still a mission
                while self.find( "VerifyGoAgain", matching=0.97, waiting_time=10000):
                    self.click()
                    self.wait(5000)
                    self.click_at(x=600, y=300)
                    self.wait(10000)
                    self.key_f9()
                    self.wait(5000)
                    if self.find( "ctrlShiftU", matching=0.97, waiting_time=10000):
                        self.click()
                        self.wait(15000)
                        self.control_w()
                        self.control_w()
                    else:
                        self.not_found("ctrlShiftU")

                # Closes reward Page
                self.scroll_up(clicks=150)
                if self.find( "closeReward", matching=0.97, waiting_time=10000):
                    self.click()
                else:
                    self.not_found("closeReward")

                # Water
                if self.find( "water", matching=0.97, waiting_time=10000):
                    self.click()
                else:
                    self.not_found("water")

                # Closes E-tree
                if self.find( "closeEtree", matching=0.97, waiting_time=10000):
                    self.click()
                else:
                    self.not_found("closeEtree")
            else:
                self.not_found("rewardPage")
        else:
            self.not_found("e-tree")

        # Opens E-tree mission in temperature
        self.control_t()
        self.wait(1000)
        self.click_at(1155, 125)
        self.wait(1000)
        self.click_at(1065, 175)

        if not self.find( "msStart", matching=0.97, waiting_time=10000):
            self.not_found("msStart")
        self.wait(5000)

        if self.find( "closeMissionComponent", matching=0.97, waiting_time=10000):
            self.click()
        else:
            self.not_found("closeMissionComponent")

        # Climate notice mission
        # Scroll down
        self.click_at(1315, 675)
        self.wait(1000)
        self.click_at(1315, 675)

        # News click
        self.wait(1000)
        self.click_at(305, 430)

        # Close news
        self.wait(10000)
        self.control_w()

        # Scroll up
        self.click_at(1315, 135)
        self.wait(2000)
        self.click_at(1315, 135)

        if self.find( "closeMissionComponent", matching=0.97, waiting_time=10000):
            self.click()
        else:
            self.not_found("closeMissionComponent")

        # Report Weather Mission
        # Agreement 1
        if self.find( "reportAgree", matching=0.97, waiting_time=10000):
            self.click()
        else:
            self.not_found("reportAgree")

            # Agreement 2
            if self.find( "reportAgreeTwo", matching=0.97, waiting_time=10000):
                self.click()
            else:
                self.not_found("reportAgreeTwo")

                # Report page "see"
                if self.find( "reportPageSee", matching=0.97, waiting_time=10000):
                    self.click()
                    if not self.find( "reportPartlySunny", matching=0.97, waiting_time=10000):
                        self.not_found("reportPartlySunny")
                    self.click()
                    if not self.find( "reportSend", matching=0.97, waiting_time=10000):
                        self.not_found("reportSend")
                    self.click()
                else:
                    self.not_found("reportPageSee")

                    # Report page normal
                    if self.find( "reportPage", matching=0.97, waiting_time=10000):
                        self.click()
                        if not self.find( "reportPartlySunny", matching=0.97, waiting_time=10000):
                            self.not_found("reportPartlySunny")
                        self.click()
                        if not self.find( "reportSend", matching=0.97, waiting_time=10000):
                            self.not_found("reportSend")
                        self.click()
                    else:
                        self.not_found("reportPage")

        if self.find( "closeMissionComponent", matching=0.97, waiting_time=10000):
            self.click()
        self.not_found("closeMissionComponent")

        # Secret map mission
        #self.click_at(910, 565)
        if self.find( "openMap", matching=0.97, waiting_time=10000):
            self.click()
            if not self.find( "msStart", matching=0.97, waiting_time=10000):
                self.not_found("msStart")
            if self.find( "coldZoomOut", matching=0.97, waiting_time=10000):
                for i in range(5):
                    self.click()
                    self.wait(500)

                self.wait(1000)
                self.mouse_move(885, 325)
                self.mouse_down()
                self.mouse_move(885, 675)
                self.mouse_up()
            else:
                self.not_found("coldZoomOut")

            if self.find( "mapRay", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(2000)
            else:
                self.not_found("mapRay")

            if self.find( "mapCaution", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)

                self.click_at(510, 400)
                self.wait(2000)
                self.click_at(955, 375)
                self.wait(2000)
                self.click_at(1245, 325)
                self.wait(2000)
            else:
                self.not_found("mapCaution")

            if self.find( "mapSnow", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapSnow")

            if self.find( "mapCyclone", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapCyclone")

            if self.find( "mapAirQa", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapAirQa")

            if self.find( "mapPoint", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapPoint")

            if self.find( "mapSeaPressure", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapSeaPressure")

            if self.find( "mapVisibility", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapVisibility")

            if self.find( "mapMoisture", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapMoisture")

            if self.find( "mapCloud", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapCloud")

            if self.find( "mapWind", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
                self.click_at(675, 305)
                self.wait(3000)
                self.click_at(580, 290)
                self.wait(3000)
                self.click_at(775, 325)
                self.wait(3000)
            else:
                self.not_found("mapWind")

            if self.find( "mapRadar", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapRadar")

            if self.find( "mapRain", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapRain")

            if self.find( "mapTemperature", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(5000)
                self.click_at(915, 605)
                self.wait(3000)
                self.click_at(1035, 625)
                self.wait(3000)
                self.click_at(675, 305)
                self.wait(3000)
                self.click_at(985, 230)
                self.wait(3000)
                self.click_at(525, 300)
                self.wait(3000)
            else:
                self.not_found("mapTemperature")

            if self.find( "mapTree", matching=0.97, waiting_time=10000):
                self.click()
                self.wait(3000)
            else:
                self.not_found("mapTree")
        else:
            self.not_found("openMap")

        self.control_w()
        self.control_w()
        self.control_w()

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()


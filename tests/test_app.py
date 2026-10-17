
import subprocess
import unittest


class TestApplication(unittest.TestCase):

    def test_student_information(self):
        process = subprocess.Popen(
            ["python3", "-u", "app/app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        try:
            output = ""
            for _ in range(8):
                output += process.stdout.readline()

            self.assertIn("Name: Yeldos", output)
            self.assertIn("Surname: Taipakov", output)
            self.assertIn("Student ID: 38321", output)
            self.assertIn("Application is running successfully!", output)
        finally:
            process.terminate()
            process.wait(timeout=5)


if __name__ == "__main__":
    unittest.main()

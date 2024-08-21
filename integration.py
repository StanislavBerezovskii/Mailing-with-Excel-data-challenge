import subprocess


def run_mailing_robot(task: str = None):
    command = ["rcc", "run"]

    if task:
        command.extend(["-t", task])

    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

    if result.returncode == 0:
        return result.stdout
    else:
        print("Error running robot:")
        print(result.stderr)


if __name__ == "__main__":
    run_mailing_robot(task="Run Task")

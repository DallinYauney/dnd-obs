class Response:
    def __init__(
            self,
            text="",
            version="HTTP/1.1",
            code=200,
            reason="Ok",
            headers=None,
            ):
        self.text = text
        self.version = version
        self.code = code
        self.reason = reason
        self.headers = {} if headers is None else headers

    def __str__(self):
        return self.stringify(False)

    def preview(self):
        return self.stringify(True)

    def stringify(self, shorten):
        output = f"{self.version} {self.code} {self.reason}\n"
        for item in self.headers:
            output += f"{item}: {self.headers[item]}\n"

        output += "\n"
        body = self.text.split("\n")[:-1]
        if shorten and len(body) > 4:
            output += f"{body[0]}\n{body[1]}\n. . .\n{body[-2]}\n{body[-1]}"
        else:
            output += self.text

        return output

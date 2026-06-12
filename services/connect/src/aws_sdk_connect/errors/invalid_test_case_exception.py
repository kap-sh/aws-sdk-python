"""Generated from Smithy shape ``com.amazonaws.connect#InvalidTestCaseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.problems


class InvalidTestCaseException_(TypedDict):
    problems: NotRequired["aws_sdk_connect.types.problems.Problems"]
    """<p>The problems with the test. Please fix before trying again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidTestCaseException_) -> dict:
    out: dict = {}
    if "problems" in value:
        import aws_sdk_connect.types.problems

        out["Problems"] = aws_sdk_connect.types.problems.serialize_json(
            value["problems"]
        )
    return out


def deserialize_json(data: dict) -> InvalidTestCaseException_:
    out: InvalidTestCaseException_ = {}  # type: ignore[typeddict-item]
    if "Problems" in data:
        import aws_sdk_connect.types.problems

        out["problems"] = aws_sdk_connect.types.problems.deserialize_json(
            data["Problems"]
        )
    return out


class InvalidTestCaseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidTestCaseException``."""

    code: str | None = "InvalidTestCaseException"

    def __init__(self, data: InvalidTestCaseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidTestCaseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidTestCaseException":
        return cls(deserialize_json(data))

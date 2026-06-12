"""Generated from Smithy shape ``com.amazonaws.ssm#UnsupportedCalendarException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class UnsupportedCalendarException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedCalendarException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedCalendarException_:
    out: UnsupportedCalendarException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedCalendarException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#UnsupportedCalendarException``."""

    code: str | None = "UnsupportedCalendarException"

    def __init__(self, data: UnsupportedCalendarException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedCalendarException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedCalendarException":
        return cls(deserialize_aws_json_1_1(data))

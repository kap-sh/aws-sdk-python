"""Generated from Smithy shape ``com.amazonaws.workmail#InvalidPasswordException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class InvalidPasswordException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPasswordException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPasswordException_:
    out: InvalidPasswordException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidPasswordException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#InvalidPasswordException``."""

    code: str | None = "InvalidPasswordException"

    def __init__(self, data: InvalidPasswordException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPasswordException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPasswordException":
        return cls(deserialize_aws_json_1_1(data))

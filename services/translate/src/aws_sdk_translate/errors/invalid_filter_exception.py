"""Generated from Smithy shape ``com.amazonaws.translate#InvalidFilterException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_translate.types.string


class InvalidFilterException_(TypedDict):
    message: NotRequired["aws_sdk_translate.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidFilterException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidFilterException_:
    out: InvalidFilterException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidFilterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#InvalidFilterException``."""

    code: str | None = "InvalidFilterException"

    def __init__(self, data: InvalidFilterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidFilterException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidFilterException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.acm#InvalidArgsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_acm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_acm.types.string


class InvalidArgsException_(TypedDict):
    message: NotRequired["aws_sdk_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidArgsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidArgsException_:
    out: InvalidArgsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidArgsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acm#InvalidArgsException``."""

    code: str | None = "InvalidArgsException"

    def __init__(self, data: InvalidArgsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArgsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidArgsException":
        return cls(deserialize_aws_json_1_1(data))

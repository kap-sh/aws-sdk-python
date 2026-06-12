"""Generated from Smithy shape ``com.amazonaws.acm#InvalidArnException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_acm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_acm.types.string


class InvalidArnException_(TypedDict):
    message: NotRequired["aws_sdk_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidArnException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidArnException_:
    out: InvalidArnException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acm#InvalidArnException``."""

    code: str | None = "InvalidArnException"

    def __init__(self, data: InvalidArnException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArnException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidArnException":
        return cls(deserialize_aws_json_1_1(data))

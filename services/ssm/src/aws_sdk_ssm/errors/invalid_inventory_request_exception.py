"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidInventoryRequestException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidInventoryRequestException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInventoryRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInventoryRequestException_:
    out: InvalidInventoryRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidInventoryRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidInventoryRequestException``."""

    code: str | None = "InvalidInventoryRequestException"

    def __init__(self, data: InvalidInventoryRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInventoryRequestException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInventoryRequestException":
        return cls(deserialize_aws_json_1_1(data))

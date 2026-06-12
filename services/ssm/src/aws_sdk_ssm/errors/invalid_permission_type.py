"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidPermissionType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidPermissionType_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPermissionType_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPermissionType_:
    out: InvalidPermissionType_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidPermissionType(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidPermissionType``."""

    code: str | None = "InvalidPermissionType"

    def __init__(self, data: InvalidPermissionType_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPermissionType",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPermissionType":
        return cls(deserialize_aws_json_1_1(data))

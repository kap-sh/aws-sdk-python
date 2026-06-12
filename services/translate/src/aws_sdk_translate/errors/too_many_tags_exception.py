"""Generated from Smithy shape ``com.amazonaws.translate#TooManyTagsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_translate.types.resource_arn
    import aws_sdk_translate.types.string


class TooManyTagsException_(TypedDict):
    message: NotRequired["aws_sdk_translate.types.string.String"]
    resource_arn: NotRequired["aws_sdk_translate.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(self, data: TooManyTagsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TooManyTagsException":
        return cls(deserialize_aws_json_1_1(data))

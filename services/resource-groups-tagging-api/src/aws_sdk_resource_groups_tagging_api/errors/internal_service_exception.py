"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#InternalServiceException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resource_groups_tagging_api.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.exception_message


class InternalServiceException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServiceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServiceException_:
    out: InternalServiceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resourcegroupstaggingapi#InternalServiceException``."""

    code: str | None = "InternalServiceException"

    def __init__(self, data: InternalServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServiceException":
        return cls(deserialize_aws_json_1_1(data))

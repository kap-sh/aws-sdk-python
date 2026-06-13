"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ResourceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.resource_type


class ResourceNotFoundException_(TypedDict):
    message: NotRequired["str"]
    resource_type: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.resource_type.ResourceType"
    ]
    """<p>The type of resource that caused the exception.</p>"""
    resource_id: NotRequired["str"]
    """<p>The unique identifier of the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceNotFoundException_:
    out: ResourceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out


class ResourceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ResourceNotFoundException``."""

    code: str | None = "ResourceNotFoundException"

    def __init__(self, data: ResourceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ResourceNotFoundException":
        return cls(deserialize_aws_json_1_0(data))

"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.conflict_exception_reason
    import aws_sdk_pinpoint_sms_voice_v2.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.conflict_exception_reason.ConflictExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""
    resource_type: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.resource_type.ResourceType"
    ]
    """<p>The type of resource that caused the exception.</p>"""
    resource_id: NotRequired["str"]
    """<p>The unique identifier of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data))

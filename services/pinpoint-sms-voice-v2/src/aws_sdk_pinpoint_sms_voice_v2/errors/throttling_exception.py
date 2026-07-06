"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ThrottlingException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data))

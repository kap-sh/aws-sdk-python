"""Generated from Smithy shape ``com.amazonaws.inspector#UnsupportedFeatureException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.bool
    import aws_sdk_inspector.types.error_message


class UnsupportedFeatureException_(TypedDict):
    message: "aws_sdk_inspector.types.error_message.ErrorMessage"
    can_retry: "aws_sdk_inspector.types.bool.Bool"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedFeatureException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["canRetry"] = value["can_retry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedFeatureException_:
    out: UnsupportedFeatureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("UnsupportedFeatureException_.message required")
    if "canRetry" in data:
        out["can_retry"] = data["canRetry"]
    else:
        raise DeserializationError("UnsupportedFeatureException_.can_retry required")
    return out


class UnsupportedFeatureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#UnsupportedFeatureException``."""

    code: str | None = "UnsupportedFeatureException"

    def __init__(self, data: UnsupportedFeatureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedFeatureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedFeatureException":
        return cls(deserialize_aws_json_1_1(data))

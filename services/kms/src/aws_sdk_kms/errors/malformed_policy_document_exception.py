"""Generated from Smithy shape ``com.amazonaws.kms#MalformedPolicyDocumentException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class MalformedPolicyDocumentException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MalformedPolicyDocumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MalformedPolicyDocumentException_:
    out: MalformedPolicyDocumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MalformedPolicyDocumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#MalformedPolicyDocumentException``."""

    code: str | None = "MalformedPolicyDocumentException"

    def __init__(self, data: MalformedPolicyDocumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedPolicyDocumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MalformedPolicyDocumentException":
        return cls(deserialize_aws_json_1_1(data))

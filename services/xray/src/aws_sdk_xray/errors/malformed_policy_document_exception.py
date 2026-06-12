"""Generated from Smithy shape ``com.amazonaws.xray#MalformedPolicyDocumentException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_xray.types.error_message


class MalformedPolicyDocumentException_(TypedDict):
    message: NotRequired["aws_sdk_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MalformedPolicyDocumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MalformedPolicyDocumentException_:
    out: MalformedPolicyDocumentException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class MalformedPolicyDocumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#MalformedPolicyDocumentException``."""

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
    def from_json(cls, data: dict) -> "MalformedPolicyDocumentException":
        return cls(deserialize_json(data))

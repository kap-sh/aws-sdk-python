"""Generated from Smithy shape ``com.amazonaws.inspector#PreviewGenerationInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_inspector.types.error_message


class PreviewGenerationInProgressException_(TypedDict, closed=True):
    message: "capo_inspector.types.error_message.ErrorMessage"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreviewGenerationInProgressException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviewGenerationInProgressException_:
    out: PreviewGenerationInProgressException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "PreviewGenerationInProgressException_.message required"
        )
    return out


class PreviewGenerationInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.inspector#PreviewGenerationInProgressException``."""

    code: str | None = "PreviewGenerationInProgressException"

    def __init__(self, data: PreviewGenerationInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreviewGenerationInProgressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PreviewGenerationInProgressException":
        return cls(deserialize_aws_json_1_1(data))

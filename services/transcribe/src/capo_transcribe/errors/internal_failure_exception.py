"""Generated from Smithy shape ``com.amazonaws.transcribe#InternalFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import ServiceError

if TYPE_CHECKING:
    import capo_transcribe.types.string


class InternalFailureException_(TypedDict, closed=True):
    message: NotRequired["capo_transcribe.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transcribe#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(self, data: InternalFailureException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalFailureException":
        return cls(deserialize_aws_json_1_1(data))

"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ResourceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_voice.errors import ServiceError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.error_code
    import capo_chime_sdk_voice.types.string


class ResourceLimitExceededException_(TypedDict, closed=True):
    code: NotRequired["capo_chime_sdk_voice.types.error_code.ErrorCode"]
    message: NotRequired["capo_chime_sdk_voice.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_chime_sdk_voice.types.error_code

        out["Code"] = capo_chime_sdk_voice.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_chime_sdk_voice.types.error_code

        out["code"] = capo_chime_sdk_voice.types.error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkvoice#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(self, data: ResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceLimitExceededException":
        return cls(deserialize_json(data))

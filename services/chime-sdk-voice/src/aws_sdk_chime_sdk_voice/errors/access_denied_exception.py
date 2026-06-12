"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_voice.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.error_code
    import aws_sdk_chime_sdk_voice.types.string


class AccessDeniedException_(TypedDict):
    code: NotRequired["aws_sdk_chime_sdk_voice.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_chime_sdk_voice.types.error_code

        out["Code"] = aws_sdk_chime_sdk_voice.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_chime_sdk_voice.types.error_code

        out["code"] = aws_sdk_chime_sdk_voice.types.error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkvoice#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))

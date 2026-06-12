"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GoneException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_voice.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.error_code
    import aws_sdk_chime_sdk_voice.types.string


class GoneException_(TypedDict):
    code: NotRequired["aws_sdk_chime_sdk_voice.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: GoneException_) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_chime_sdk_voice.types.error_code

        out["Code"] = aws_sdk_chime_sdk_voice.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GoneException_:
    out: GoneException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_chime_sdk_voice.types.error_code

        out["code"] = aws_sdk_chime_sdk_voice.types.error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class GoneException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkvoice#GoneException``."""

    code: str | None = "GoneException"

    def __init__(self, data: GoneException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GoneException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "GoneException":
        return cls(deserialize_json(data))

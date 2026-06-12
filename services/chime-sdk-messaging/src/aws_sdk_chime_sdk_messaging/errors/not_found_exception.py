"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#NotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_messaging.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.error_code
    import aws_sdk_chime_sdk_messaging.types.string


class NotFoundException_(TypedDict):
    code: NotRequired["aws_sdk_chime_sdk_messaging.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime_sdk_messaging.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: NotFoundException_) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_chime_sdk_messaging.types.error_code

        out["Code"] = aws_sdk_chime_sdk_messaging.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_chime_sdk_messaging.types.error_code

        out["code"] = aws_sdk_chime_sdk_messaging.types.error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmessaging#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_json(data))

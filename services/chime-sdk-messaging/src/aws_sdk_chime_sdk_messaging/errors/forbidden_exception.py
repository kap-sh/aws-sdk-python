"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ForbiddenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_messaging.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.error_code
    import aws_sdk_chime_sdk_messaging.types.string


class ForbiddenException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_chime_sdk_messaging.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_chime_sdk_messaging.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_chime_sdk_messaging.types.error_code

        out["Code"] = aws_sdk_chime_sdk_messaging.types.error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_chime_sdk_messaging.types.error_code

        out["code"] = aws_sdk_chime_sdk_messaging.types.error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chimesdkmessaging#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(self, data: ForbiddenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ForbiddenException":
        return cls(deserialize_json(data))

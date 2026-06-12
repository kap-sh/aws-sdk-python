"""Generated from Smithy shape ``com.amazonaws.iot#SqlParseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message2


class SqlParseException_(TypedDict):
    message: NotRequired["aws_sdk_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqlParseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SqlParseException_:
    out: SqlParseException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SqlParseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#SqlParseException``."""

    code: str | None = "SqlParseException"

    def __init__(self, data: SqlParseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SqlParseException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SqlParseException":
        return cls(deserialize_json(data))

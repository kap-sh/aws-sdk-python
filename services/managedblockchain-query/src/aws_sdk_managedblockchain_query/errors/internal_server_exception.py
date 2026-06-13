"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#InternalServerException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.exception_message


class InternalServerException_(TypedDict):
    message: "aws_sdk_managedblockchain_query.types.exception_message.ExceptionMessage"
    """<p>The container for the exception message.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>Specifies the <code>retryAfterSeconds</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchainquery#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_json(data))

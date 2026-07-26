"""Generated from Smithy shape ``com.amazonaws.clouddirectory#SchemaAlreadyPublishedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class SchemaAlreadyPublishedException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaAlreadyPublishedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SchemaAlreadyPublishedException_:
    out: SchemaAlreadyPublishedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SchemaAlreadyPublishedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#SchemaAlreadyPublishedException``."""

    code: str | None = "SchemaAlreadyPublishedException"

    def __init__(self, data: SchemaAlreadyPublishedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SchemaAlreadyPublishedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SchemaAlreadyPublishedException":
        return cls(deserialize_json(data))

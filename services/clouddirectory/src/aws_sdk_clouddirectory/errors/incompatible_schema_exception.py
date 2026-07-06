"""Generated from Smithy shape ``com.amazonaws.clouddirectory#IncompatibleSchemaException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.exception_message


class IncompatibleSchemaException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleSchemaException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IncompatibleSchemaException_:
    out: IncompatibleSchemaException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IncompatibleSchemaException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#IncompatibleSchemaException``."""

    code: str | None = "IncompatibleSchemaException"

    def __init__(self, data: IncompatibleSchemaException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleSchemaException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IncompatibleSchemaException":
        return cls(deserialize_json(data))

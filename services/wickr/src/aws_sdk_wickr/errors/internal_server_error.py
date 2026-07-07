"""Generated from Smithy shape ``com.amazonaws.wickr#InternalServerError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class InternalServerError_(TypedDict, closed=True):
    message: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>A message describing the internal server error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerError_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerError_.message required")
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(self, data: InternalServerError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InternalServerError":
        return cls(deserialize_json(data))

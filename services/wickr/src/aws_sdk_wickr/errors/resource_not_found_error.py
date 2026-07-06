"""Generated from Smithy shape ``com.amazonaws.wickr#ResourceNotFoundError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class ResourceNotFoundError_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message identifying which resource was not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotFoundError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotFoundError_:
    out: ResourceNotFoundError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceNotFoundError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wickr#ResourceNotFoundError``."""

    code: str | None = "ResourceNotFoundError"

    def __init__(self, data: ResourceNotFoundError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotFoundError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNotFoundError":
        return cls(deserialize_json(data))

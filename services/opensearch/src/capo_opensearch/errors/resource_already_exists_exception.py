"""Generated from Smithy shape ``com.amazonaws.opensearch#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import ServiceError

if TYPE_CHECKING:
    import capo_opensearch.types.error_message


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_opensearch.types.error_message.ErrorMessage"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearch#ResourceAlreadyExistsException``."""

    code: str | None = "ResourceAlreadyExistsException"

    def __init__(self, data: ResourceAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceAlreadyExistsException":
        return cls(deserialize_json(data))

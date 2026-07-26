"""Generated from Smithy shape ``com.amazonaws.mpa#TooManyTagsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mpa.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_mpa.types.string


class TooManyTagsException_(TypedDict, closed=True):
    message: "capo_mpa.types.string.String"
    """<p>Message for the <code>TooManyTagsException</code> error.</p>"""
    resource_name: NotRequired["capo_mpa.types.string.String"]
    """<p>Name of the resource for the <code>TooManyTagsException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyTagsException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("TooManyTagsException_.message required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mpa#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(self, data: TooManyTagsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyTagsException":
        return cls(deserialize_json(data))

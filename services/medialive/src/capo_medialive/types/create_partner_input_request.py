"""Generated from Smithy shape ``com.amazonaws.medialive#CreatePartnerInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.tags


class CreatePartnerInputRequest(TypedDict, closed=True):
    input_id: "capo_medialive.types.__string.__string"
    """Unique ID of the input."""
    request_id: NotRequired["capo_medialive.types.__string.__string"]
    """Unique identifier of the request to ensure the request is handled exactly once in case of retries."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePartnerInputRequest) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePartnerInputRequest:
    out: CreatePartnerInputRequest = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    return out

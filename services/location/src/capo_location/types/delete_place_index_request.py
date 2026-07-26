"""Generated from Smithy shape ``com.amazonaws.location#DeletePlaceIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.resource_name


class DeletePlaceIndexRequest(TypedDict, closed=True):
    index_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePlaceIndexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePlaceIndexRequest:
    out: DeletePlaceIndexRequest = {}  # type: ignore[typeddict-item]
    return out

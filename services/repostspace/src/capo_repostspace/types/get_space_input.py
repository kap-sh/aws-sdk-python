"""Generated from Smithy shape ``com.amazonaws.repostspace#GetSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.space_id


class GetSpaceInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The ID of the private re:Post.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpaceInput:
    out: GetSpaceInput = {}  # type: ignore[typeddict-item]
    return out

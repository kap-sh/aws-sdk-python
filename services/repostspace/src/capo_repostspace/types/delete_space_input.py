"""Generated from Smithy shape ``com.amazonaws.repostspace#DeleteSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.space_id


class DeleteSpaceInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSpaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSpaceInput:
    out: DeleteSpaceInput = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.repostspace#GetSpaceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.space_id


class GetSpaceInput(TypedDict):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The ID of the private re:Post.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpaceInput:
    out: GetSpaceInput = {}  # type: ignore[typeddict-item]
    return out

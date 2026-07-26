"""Generated from Smithy shape ``com.amazonaws.synthetics#CreateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.group


class CreateGroupResponse(TypedDict, closed=True):
    group: NotRequired["capo_synthetics.types.group.Group"]
    """<p>A structure that contains information about the group that was just created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_synthetics.types.group

        out["Group"] = capo_synthetics.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_synthetics.types.group

        out["group"] = capo_synthetics.types.group.deserialize_json(data["Group"])
    return out

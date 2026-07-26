"""Generated from Smithy shape ``com.amazonaws.xray#CreateGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.group


class CreateGroupResult(TypedDict, closed=True):
    group: NotRequired["capo_xray.types.group.Group"]
    """<p>The group that was created. Contains the name of the group that was created, the Amazon Resource Name (ARN) of the group that was generated based on the group name, the filter expression, and the insight configuration that was assigned to the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupResult) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_xray.types.group

        out["Group"] = capo_xray.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> CreateGroupResult:
    out: CreateGroupResult = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_xray.types.group

        out["group"] = capo_xray.types.group.deserialize_json(data["Group"])
    return out

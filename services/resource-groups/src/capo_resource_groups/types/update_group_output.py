"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UpdateGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group


class UpdateGroupOutput(TypedDict, closed=True):
    group: NotRequired["capo_resource_groups.types.group.Group"]
    """<p>The update description of the resource group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupOutput) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_resource_groups.types.group

        out["Group"] = capo_resource_groups.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> UpdateGroupOutput:
    out: UpdateGroupOutput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_resource_groups.types.group

        out["group"] = capo_resource_groups.types.group.deserialize_json(data["Group"])
    return out

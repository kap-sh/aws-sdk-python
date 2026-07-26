"""Generated from Smithy shape ``com.amazonaws.resourcegroups#DeleteGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group


class DeleteGroupOutput(TypedDict, closed=True):
    group: NotRequired["capo_resource_groups.types.group.Group"]
    """<p>A full description of the deleted resource group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGroupOutput) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_resource_groups.types.group

        out["Group"] = capo_resource_groups.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> DeleteGroupOutput:
    out: DeleteGroupOutput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_resource_groups.types.group

        out["group"] = capo_resource_groups.types.group.deserialize_json(data["Group"])
    return out

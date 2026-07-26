"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_layout_group_member_list
    import capo_quicksight.types.short_restrictive_resource_id


class SheetLayoutGroup(TypedDict, closed=True):
    id: "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>A unique identifier for the group.</p>"""
    members: "capo_quicksight.types.sheet_layout_group_member_list.SheetLayoutGroupMemberList"
    """<p>The members of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutGroup) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_quicksight.types.sheet_layout_group_member_list

    out["Members"] = (
        capo_quicksight.types.sheet_layout_group_member_list.serialize_json(
            value["members"]
        )
    )
    return out


def deserialize_json(data: dict) -> SheetLayoutGroup:
    out: SheetLayoutGroup = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SheetLayoutGroup.id required")
    if "Members" in data:
        import capo_quicksight.types.sheet_layout_group_member_list

        out["members"] = (
            capo_quicksight.types.sheet_layout_group_member_list.deserialize_json(
                data["Members"]
            )
        )
    else:
        raise DeserializationError("SheetLayoutGroup.members required")
    return out

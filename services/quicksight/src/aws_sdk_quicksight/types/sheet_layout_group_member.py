"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroupMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_layout_group_member_type
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class SheetLayoutGroupMember(TypedDict, closed=True):
    id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of the group member.</p>"""
    type: "aws_sdk_quicksight.types.sheet_layout_group_member_type.SheetLayoutGroupMemberType"
    """<p>The type of the group member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetLayoutGroupMember) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_quicksight.types.sheet_layout_group_member_type

    out["Type"] = (
        aws_sdk_quicksight.types.sheet_layout_group_member_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> SheetLayoutGroupMember:
    out: SheetLayoutGroupMember = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SheetLayoutGroupMember.id required")
    if "Type" in data:
        import aws_sdk_quicksight.types.sheet_layout_group_member_type

        out["type"] = (
            aws_sdk_quicksight.types.sheet_layout_group_member_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("SheetLayoutGroupMember.type required")
    return out

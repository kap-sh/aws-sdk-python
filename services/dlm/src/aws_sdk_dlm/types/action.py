"""Generated from Smithy shape ``com.amazonaws.dlm#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.action_name
    import aws_sdk_dlm.types.cross_region_copy_action_list


class Action(TypedDict, closed=True):
    name: NotRequired["aws_sdk_dlm.types.action_name.ActionName"]
    """<p>A descriptive name for the action.</p>"""
    cross_region_copy: NotRequired[
        "aws_sdk_dlm.types.cross_region_copy_action_list.CrossRegionCopyActionList"
    ]
    """<p>The rule for copying shared snapshots across Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "cross_region_copy" in value:
        import aws_sdk_dlm.types.cross_region_copy_action_list

        out["CrossRegionCopy"] = (
            aws_sdk_dlm.types.cross_region_copy_action_list.serialize_json(
                value["cross_region_copy"]
            )
        )
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CrossRegionCopy" in data:
        import aws_sdk_dlm.types.cross_region_copy_action_list

        out["cross_region_copy"] = (
            aws_sdk_dlm.types.cross_region_copy_action_list.deserialize_json(
                data["CrossRegionCopy"]
            )
        )
    return out

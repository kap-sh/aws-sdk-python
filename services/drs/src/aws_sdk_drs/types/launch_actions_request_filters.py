"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_ids


class LaunchActionsRequestFilters(TypedDict, closed=True):
    action_ids: NotRequired["aws_sdk_drs.types.launch_action_ids.LaunchActionIds"]
    """<p>Launch actions Ids.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionsRequestFilters) -> dict:
    out: dict = {}
    if "action_ids" in value:
        import aws_sdk_drs.types.launch_action_ids

        out["actionIds"] = aws_sdk_drs.types.launch_action_ids.serialize_json(
            value["action_ids"]
        )
    return out


def deserialize_json(data: dict) -> LaunchActionsRequestFilters:
    out: LaunchActionsRequestFilters = {}  # type: ignore[typeddict-item]
    if "actionIds" in data:
        import aws_sdk_drs.types.launch_action_ids

        out["action_ids"] = aws_sdk_drs.types.launch_action_ids.deserialize_json(
            data["actionIds"]
        )
    return out

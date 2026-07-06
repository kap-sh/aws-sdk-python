"""Generated from Smithy shape ``com.amazonaws.mgn#SourceServerActionsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.action_i_ds


class SourceServerActionsRequestFilters(TypedDict, closed=True):
    action_i_ds: NotRequired["aws_sdk_mgn.types.action_i_ds.ActionIDs"]
    """<p>Action IDs to filter source server post migration custom actions by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerActionsRequestFilters) -> dict:
    out: dict = {}
    if "action_i_ds" in value:
        import aws_sdk_mgn.types.action_i_ds

        out["actionIDs"] = aws_sdk_mgn.types.action_i_ds.serialize_json(
            value["action_i_ds"]
        )
    return out


def deserialize_json(data: dict) -> SourceServerActionsRequestFilters:
    out: SourceServerActionsRequestFilters = {}  # type: ignore[typeddict-item]
    if "actionIDs" in data:
        import aws_sdk_mgn.types.action_i_ds

        out["action_i_ds"] = aws_sdk_mgn.types.action_i_ds.deserialize_json(
            data["actionIDs"]
        )
    return out

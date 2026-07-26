"""Generated from Smithy shape ``com.amazonaws.xray#GetGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.group


class GetGroupResult(TypedDict, closed=True):
    group: NotRequired["capo_xray.types.group.Group"]
    """<p>The group that was requested. Contains the name of the group, the ARN of the group, the filter expression, and the insight configuration assigned to the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupResult) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_xray.types.group

        out["Group"] = capo_xray.types.group.serialize_json(value["group"])
    return out


def deserialize_json(data: dict) -> GetGroupResult:
    out: GetGroupResult = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_xray.types.group

        out["group"] = capo_xray.types.group.deserialize_json(data["Group"])
    return out

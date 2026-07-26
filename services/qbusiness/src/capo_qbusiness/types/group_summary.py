"""Generated from Smithy shape ``com.amazonaws.qbusiness#GroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.group_name


class GroupSummary(TypedDict, closed=True):
    group_name: NotRequired["capo_qbusiness.types.group_name.GroupName"]
    """<p>The name of the group the summary information is for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummary) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    return out


def deserialize_json(data: dict) -> GroupSummary:
    out: GroupSummary = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    return out

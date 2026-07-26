"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.group
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class CreateGroupResponse(TypedDict, closed=True):
    group: NotRequired["capo_quicksight.types.group.Group"]
    """<p>The name of the group.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import capo_quicksight.types.group

        out["Group"] = capo_quicksight.types.group.serialize_json(value["group"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateGroupResponse:
    out: CreateGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import capo_quicksight.types.group

        out["group"] = capo_quicksight.types.group.deserialize_json(data["Group"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

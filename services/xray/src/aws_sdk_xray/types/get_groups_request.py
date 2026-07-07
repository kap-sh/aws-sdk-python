"""Generated from Smithy shape ``com.amazonaws.xray#GetGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.get_groups_next_token


class GetGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_xray.types.get_groups_next_token.GetGroupsNextToken"
    ]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetGroupsRequest:
    out: GetGroupsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

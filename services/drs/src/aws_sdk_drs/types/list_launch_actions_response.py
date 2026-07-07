"""Generated from Smithy shape ``com.amazonaws.drs#ListLaunchActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_actions
    import aws_sdk_drs.types.pagination_token


class ListLaunchActionsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_drs.types.launch_actions.LaunchActions"]
    """<p>List of resource launch actions.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>Next token returned when listing resource launch actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLaunchActionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_drs.types.launch_actions

        out["items"] = aws_sdk_drs.types.launch_actions.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLaunchActionsResponse:
    out: ListLaunchActionsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_drs.types.launch_actions

        out["items"] = aws_sdk_drs.types.launch_actions.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

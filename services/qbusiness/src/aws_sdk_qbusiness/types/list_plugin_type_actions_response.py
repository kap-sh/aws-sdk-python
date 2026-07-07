"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginTypeActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.actions
    import aws_sdk_qbusiness.types.next_token


class ListPluginTypeActionsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of plugins.</p>"""
    items: NotRequired["aws_sdk_qbusiness.types.actions.Actions"]
    """<p>An array of information on one or more plugins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginTypeActionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_qbusiness.types.actions

        out["items"] = aws_sdk_qbusiness.types.actions.serialize_json(value["items"])
    return out


def deserialize_json(data: dict) -> ListPluginTypeActionsResponse:
    out: ListPluginTypeActionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_qbusiness.types.actions

        out["items"] = aws_sdk_qbusiness.types.actions.deserialize_json(data["items"])
    return out

"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListBridgesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_listed_bridge


class ListBridgesResponse(TypedDict, closed=True):
    bridges: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_listed_bridge.__listOfListedBridge"
    ]
    """<p> A list of bridge summaries.</p>"""
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListBridges</code> request a second time and specify the <code>NextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBridgesResponse) -> dict:
    out: dict = {}
    if "bridges" in value:
        import aws_sdk_mediaconnect.types.__list_of_listed_bridge

        out["bridges"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_bridge.serialize_json(
                value["bridges"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBridgesResponse:
    out: ListBridgesResponse = {}  # type: ignore[typeddict-item]
    if "bridges" in data:
        import aws_sdk_mediaconnect.types.__list_of_listed_bridge

        out["bridges"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_bridge.deserialize_json(
                data["bridges"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

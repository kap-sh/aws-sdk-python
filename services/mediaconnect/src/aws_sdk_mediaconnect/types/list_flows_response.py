"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListFlowsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_listed_flow


class ListFlowsResponse(TypedDict):
    flows: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_listed_flow.__listOfListedFlow"
    ]
    """<p> A list of flow summaries.</p>"""
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListFlows</code> request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListFlows</code> request a second time and specify the <code>NextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsResponse) -> dict:
    out: dict = {}
    if "flows" in value:
        import aws_sdk_mediaconnect.types.__list_of_listed_flow

        out["flows"] = aws_sdk_mediaconnect.types.__list_of_listed_flow.serialize_json(
            value["flows"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowsResponse:
    out: ListFlowsResponse = {}  # type: ignore[typeddict-item]
    if "flows" in data:
        import aws_sdk_mediaconnect.types.__list_of_listed_flow

        out["flows"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_flow.deserialize_json(
                data["flows"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

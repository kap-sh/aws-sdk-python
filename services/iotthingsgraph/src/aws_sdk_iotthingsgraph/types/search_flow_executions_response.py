"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchFlowExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_execution_summaries
    import aws_sdk_iotthingsgraph.types.next_token


class SearchFlowExecutionsResponse(TypedDict, closed=True):
    summaries: NotRequired[
        "aws_sdk_iotthingsgraph.types.flow_execution_summaries.FlowExecutionSummaries"
    ]
    """<p>An array of objects that contain summary information about each workflow execution in the result set.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchFlowExecutionsResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import aws_sdk_iotthingsgraph.types.flow_execution_summaries

        out["summaries"] = (
            aws_sdk_iotthingsgraph.types.flow_execution_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchFlowExecutionsResponse:
    out: SearchFlowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import aws_sdk_iotthingsgraph.types.flow_execution_summaries

        out["summaries"] = (
            aws_sdk_iotthingsgraph.types.flow_execution_summaries.deserialize_aws_json_1_1(
                data["summaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

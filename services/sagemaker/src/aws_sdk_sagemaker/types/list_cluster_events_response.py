"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_event_summaries
    import aws_sdk_sagemaker.types.next_token


class ListClusterEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. Include this token in subsequent <code>ListClusterEvents</code> calls to fetch more events.</p>"""
    events: NotRequired[
        "aws_sdk_sagemaker.types.cluster_event_summaries.ClusterEventSummaries"
    ]
    """<p>A list of event summaries matching the specified criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "events" in value:
        import aws_sdk_sagemaker.types.cluster_event_summaries

        out["Events"] = (
            aws_sdk_sagemaker.types.cluster_event_summaries.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterEventsResponse:
    out: ListClusterEventsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Events" in data:
        import aws_sdk_sagemaker.types.cluster_event_summaries

        out["events"] = (
            aws_sdk_sagemaker.types.cluster_event_summaries.deserialize_aws_json_1_1(
                data["Events"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListMlflowTrackingServersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.tracking_server_summary_list


class ListMlflowTrackingServersResponse(TypedDict, closed=True):
    tracking_server_summaries: NotRequired[
        "capo_sagemaker.types.tracking_server_summary_list.TrackingServerSummaryList"
    ]
    """<p>A list of tracking servers according to chosen filters.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMlflowTrackingServersResponse) -> dict:
    out: dict = {}
    if "tracking_server_summaries" in value:
        import capo_sagemaker.types.tracking_server_summary_list

        out["TrackingServerSummaries"] = (
            capo_sagemaker.types.tracking_server_summary_list.serialize_aws_json_1_1(
                value["tracking_server_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMlflowTrackingServersResponse:
    out: ListMlflowTrackingServersResponse = {}  # type: ignore[typeddict-item]
    if "TrackingServerSummaries" in data:
        import capo_sagemaker.types.tracking_server_summary_list

        out["tracking_server_summaries"] = (
            capo_sagemaker.types.tracking_server_summary_list.deserialize_aws_json_1_1(
                data["TrackingServerSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

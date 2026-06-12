"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterSchedulerConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_scheduler_config_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListClusterSchedulerConfigsResponse(TypedDict):
    cluster_scheduler_config_summaries: NotRequired[
        "aws_sdk_sagemaker.types.cluster_scheduler_config_summary_list.ClusterSchedulerConfigSummaryList"
    ]
    """<p>Summaries of the cluster policies.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterSchedulerConfigsResponse) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_summaries" in value:
        import aws_sdk_sagemaker.types.cluster_scheduler_config_summary_list

        out["ClusterSchedulerConfigSummaries"] = (
            aws_sdk_sagemaker.types.cluster_scheduler_config_summary_list.serialize_aws_json_1_1(
                value["cluster_scheduler_config_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterSchedulerConfigsResponse:
    out: ListClusterSchedulerConfigsResponse = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigSummaries" in data:
        import aws_sdk_sagemaker.types.cluster_scheduler_config_summary_list

        out["cluster_scheduler_config_summaries"] = (
            aws_sdk_sagemaker.types.cluster_scheduler_config_summary_list.deserialize_aws_json_1_1(
                data["ClusterSchedulerConfigSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

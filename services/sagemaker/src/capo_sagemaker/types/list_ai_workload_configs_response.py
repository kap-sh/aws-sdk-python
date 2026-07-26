"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIWorkloadConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_workload_config_summary_list
    import capo_sagemaker.types.next_token


class ListAIWorkloadConfigsResponse(TypedDict, closed=True):
    ai_workload_configs: NotRequired[
        "capo_sagemaker.types.ai_workload_config_summary_list.AIWorkloadConfigSummaryList"
    ]
    """<p>An array of <code>AIWorkloadConfigSummary</code> objects, one for each AI workload configuration that matches the specified filters.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of configurations, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIWorkloadConfigsResponse) -> dict:
    out: dict = {}
    if "ai_workload_configs" in value:
        import capo_sagemaker.types.ai_workload_config_summary_list

        out["AIWorkloadConfigs"] = (
            capo_sagemaker.types.ai_workload_config_summary_list.serialize_aws_json_1_1(
                value["ai_workload_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAIWorkloadConfigsResponse:
    out: ListAIWorkloadConfigsResponse = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigs" in data:
        import capo_sagemaker.types.ai_workload_config_summary_list

        out["ai_workload_configs"] = (
            capo_sagemaker.types.ai_workload_config_summary_list.deserialize_aws_json_1_1(
                data["AIWorkloadConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

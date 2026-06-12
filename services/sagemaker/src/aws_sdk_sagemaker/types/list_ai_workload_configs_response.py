"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIWorkloadConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_workload_config_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListAIWorkloadConfigsResponse(TypedDict):
    ai_workload_configs: NotRequired[
        "aws_sdk_sagemaker.types.ai_workload_config_summary_list.AIWorkloadConfigSummaryList"
    ]
    """<p>An array of <code>AIWorkloadConfigSummary</code> objects, one for each AI workload configuration that matches the specified filters.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of configurations, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIWorkloadConfigsResponse) -> dict:
    out: dict = {}
    if "ai_workload_configs" in value:
        import aws_sdk_sagemaker.types.ai_workload_config_summary_list

        out["AIWorkloadConfigs"] = (
            aws_sdk_sagemaker.types.ai_workload_config_summary_list.serialize_aws_json_1_1(
                value["ai_workload_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAIWorkloadConfigsResponse:
    out: ListAIWorkloadConfigsResponse = {}  # type: ignore[typeddict-item]
    if "AIWorkloadConfigs" in data:
        import aws_sdk_sagemaker.types.ai_workload_config_summary_list

        out["ai_workload_configs"] = (
            aws_sdk_sagemaker.types.ai_workload_config_summary_list.deserialize_aws_json_1_1(
                data["AIWorkloadConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

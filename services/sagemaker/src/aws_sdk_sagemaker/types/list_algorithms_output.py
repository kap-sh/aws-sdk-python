"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAlgorithmsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.algorithm_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListAlgorithmsOutput(TypedDict):
    algorithm_summary_list: NotRequired[
        "aws_sdk_sagemaker.types.algorithm_summary_list.AlgorithmSummaryList"
    ]
    """<p>&gt;An array of <code>AlgorithmSummary</code> objects, each of which lists an algorithm.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAlgorithmsOutput) -> dict:
    out: dict = {}
    if "algorithm_summary_list" in value:
        import aws_sdk_sagemaker.types.algorithm_summary_list

        out["AlgorithmSummaryList"] = (
            aws_sdk_sagemaker.types.algorithm_summary_list.serialize_aws_json_1_1(
                value["algorithm_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAlgorithmsOutput:
    out: ListAlgorithmsOutput = {}  # type: ignore[typeddict-item]
    if "AlgorithmSummaryList" in data:
        import aws_sdk_sagemaker.types.algorithm_summary_list

        out["algorithm_summary_list"] = (
            aws_sdk_sagemaker.types.algorithm_summary_list.deserialize_aws_json_1_1(
                data["AlgorithmSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

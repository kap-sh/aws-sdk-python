"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAlgorithmsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_summary_list
    import capo_sagemaker.types.next_token


class ListAlgorithmsOutput(TypedDict, closed=True):
    algorithm_summary_list: NotRequired[
        "capo_sagemaker.types.algorithm_summary_list.AlgorithmSummaryList"
    ]
    """<p>&gt;An array of <code>AlgorithmSummary</code> objects, each of which lists an algorithm.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of algorithms, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAlgorithmsOutput) -> dict:
    out: dict = {}
    if "algorithm_summary_list" in value:
        import capo_sagemaker.types.algorithm_summary_list

        out["AlgorithmSummaryList"] = (
            capo_sagemaker.types.algorithm_summary_list.serialize_aws_json_1_1(
                value["algorithm_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAlgorithmsOutput:
    out: ListAlgorithmsOutput = {}  # type: ignore[typeddict-item]
    if "AlgorithmSummaryList" in data:
        import capo_sagemaker.types.algorithm_summary_list

        out["algorithm_summary_list"] = (
            capo_sagemaker.types.algorithm_summary_list.deserialize_aws_json_1_1(
                data["AlgorithmSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

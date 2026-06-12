"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_execution_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListInferenceExecutionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of inference executions. </p>"""
    inference_execution_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_execution_summaries.InferenceExecutionSummaries"
    ]
    """<p>Provides an array of information about the individual inference executions returned from the <code>ListInferenceExecutions</code> operation, including model used, inference scheduler, data configuration, and so on. </p> <note> <p>If you don't supply the <code>InferenceSchedulerName</code> request parameter, or if you supply the name of an inference scheduler that doesn't exist, <code>ListInferenceExecutions</code> returns an empty array in <code>InferenceExecutionSummaries</code>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceExecutionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "inference_execution_summaries" in value:
        import aws_sdk_lookoutequipment.types.inference_execution_summaries

        out["InferenceExecutionSummaries"] = (
            aws_sdk_lookoutequipment.types.inference_execution_summaries.serialize_aws_json_1_0(
                value["inference_execution_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceExecutionsResponse:
    out: ListInferenceExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "InferenceExecutionSummaries" in data:
        import aws_sdk_lookoutequipment.types.inference_execution_summaries

        out["inference_execution_summaries"] = (
            aws_sdk_lookoutequipment.types.inference_execution_summaries.deserialize_aws_json_1_0(
                data["InferenceExecutionSummaries"]
            )
        )
    return out

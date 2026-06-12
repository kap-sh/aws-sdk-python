"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceSchedulersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_scheduler_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListInferenceSchedulersResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of inference schedulers. </p>"""
    inference_scheduler_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_scheduler_summaries.InferenceSchedulerSummaries"
    ]
    """<p>Provides information about the specified inference scheduler, including data upload frequency, model name and ARN, and status. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceSchedulersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "inference_scheduler_summaries" in value:
        import aws_sdk_lookoutequipment.types.inference_scheduler_summaries

        out["InferenceSchedulerSummaries"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_summaries.serialize_aws_json_1_0(
                value["inference_scheduler_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceSchedulersResponse:
    out: ListInferenceSchedulersResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "InferenceSchedulerSummaries" in data:
        import aws_sdk_lookoutequipment.types.inference_scheduler_summaries

        out["inference_scheduler_summaries"] = (
            aws_sdk_lookoutequipment.types.inference_scheduler_summaries.deserialize_aws_json_1_0(
                data["InferenceSchedulerSummaries"]
            )
        )
    return out

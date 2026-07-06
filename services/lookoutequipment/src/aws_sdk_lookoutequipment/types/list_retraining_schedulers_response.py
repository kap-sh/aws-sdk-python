"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListRetrainingSchedulersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.next_token
    import aws_sdk_lookoutequipment.types.retraining_scheduler_summaries


class ListRetrainingSchedulersResponse(TypedDict, closed=True):
    retraining_scheduler_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.retraining_scheduler_summaries.RetrainingSchedulerSummaries"
    ]
    """<p>Provides information on the specified retraining scheduler, including the model name, model ARN, status, and start date. </p>"""
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p>If the number of results exceeds the maximum, this pagination token is returned. Use this token in the request to show the next page of retraining schedulers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRetrainingSchedulersResponse) -> dict:
    out: dict = {}
    if "retraining_scheduler_summaries" in value:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_summaries

        out["RetrainingSchedulerSummaries"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_summaries.serialize_aws_json_1_0(
                value["retraining_scheduler_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRetrainingSchedulersResponse:
    out: ListRetrainingSchedulersResponse = {}  # type: ignore[typeddict-item]
    if "RetrainingSchedulerSummaries" in data:
        import aws_sdk_lookoutequipment.types.retraining_scheduler_summaries

        out["retraining_scheduler_summaries"] = (
            aws_sdk_lookoutequipment.types.retraining_scheduler_summaries.deserialize_aws_json_1_0(
                data["RetrainingSchedulerSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

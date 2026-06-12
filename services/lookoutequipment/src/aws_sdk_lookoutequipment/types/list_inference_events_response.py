"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_event_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListInferenceEventsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of inference executions. </p>"""
    inference_event_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.inference_event_summaries.InferenceEventSummaries"
    ]
    """<p>Provides an array of information about the individual inference events returned from the <code>ListInferenceEvents</code> operation, including scheduler used, event start time, event end time, diagnostics, and so on. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "inference_event_summaries" in value:
        import aws_sdk_lookoutequipment.types.inference_event_summaries

        out["InferenceEventSummaries"] = (
            aws_sdk_lookoutequipment.types.inference_event_summaries.serialize_aws_json_1_0(
                value["inference_event_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceEventsResponse:
    out: ListInferenceEventsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "InferenceEventSummaries" in data:
        import aws_sdk_lookoutequipment.types.inference_event_summaries

        out["inference_event_summaries"] = (
            aws_sdk_lookoutequipment.types.inference_event_summaries.deserialize_aws_json_1_0(
                data["InferenceEventSummaries"]
            )
        )
    return out

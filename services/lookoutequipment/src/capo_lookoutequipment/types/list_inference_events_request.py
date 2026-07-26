"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListInferenceEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_scheduler_identifier
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.next_token
    import capo_lookoutequipment.types.timestamp


class ListInferenceEventsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of inference events.</p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of inference events to list. </p>"""
    inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler for the inference events listed. </p>"""
    interval_start_time: "capo_lookoutequipment.types.timestamp.Timestamp"
    """<p> Lookout for Equipment will return all the inference events with an end time equal to or greater than the start time given.</p>"""
    interval_end_time: "capo_lookoutequipment.types.timestamp.Timestamp"
    """<p>Returns all the inference events with an end start time equal to or greater than less than the end time given.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInferenceEventsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    import capo_lookoutequipment.types.timestamp

    out["IntervalStartTime"] = (
        capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["interval_start_time"]
        )
    )
    import capo_lookoutequipment.types.timestamp

    out["IntervalEndTime"] = (
        capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["interval_end_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInferenceEventsRequest:
    out: ListInferenceEventsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        raise DeserializationError(
            "ListInferenceEventsRequest.inference_scheduler_name required"
        )
    if "IntervalStartTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["interval_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["IntervalStartTime"]
            )
        )
    else:
        raise DeserializationError(
            "ListInferenceEventsRequest.interval_start_time required"
        )
    if "IntervalEndTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["interval_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["IntervalEndTime"]
            )
        )
    else:
        raise DeserializationError(
            "ListInferenceEventsRequest.interval_end_time required"
        )
    return out

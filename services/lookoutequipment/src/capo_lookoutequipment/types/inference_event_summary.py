"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.event_duration_in_seconds
    import capo_lookoutequipment.types.inference_scheduler_arn
    import capo_lookoutequipment.types.inference_scheduler_name
    import capo_lookoutequipment.types.model_metrics
    import capo_lookoutequipment.types.timestamp


class InferenceEventSummary(TypedDict, closed=True):
    inference_scheduler_arn: NotRequired[
        "capo_lookoutequipment.types.inference_scheduler_arn.InferenceSchedulerArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the inference scheduler being used for the inference event. </p>"""
    inference_scheduler_name: NotRequired[
        "capo_lookoutequipment.types.inference_scheduler_name.InferenceSchedulerName"
    ]
    """<p>The name of the inference scheduler being used for the inference events. </p>"""
    event_start_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the starting time of an inference event. </p>"""
    event_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Indicates the ending time of an inference event. </p>"""
    diagnostics: NotRequired["capo_lookoutequipment.types.model_metrics.ModelMetrics"]
    """<p> An array which specifies the names and values of all sensors contributing to an inference event.</p>"""
    event_duration_in_seconds: NotRequired[
        "capo_lookoutequipment.types.event_duration_in_seconds.EventDurationInSeconds"
    ]
    """<p> Indicates the size of an inference event in seconds. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceEventSummary) -> dict:
    out: dict = {}
    if "inference_scheduler_arn" in value:
        out["InferenceSchedulerArn"] = value["inference_scheduler_arn"]
    if "inference_scheduler_name" in value:
        out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    if "event_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["EventStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["event_start_time"]
            )
        )
    if "event_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["EventEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["event_end_time"]
            )
        )
    if "diagnostics" in value:
        out["Diagnostics"] = value["diagnostics"]
    if "event_duration_in_seconds" in value:
        out["EventDurationInSeconds"] = value["event_duration_in_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InferenceEventSummary:
    out: InferenceEventSummary = {}  # type: ignore[typeddict-item]
    if "InferenceSchedulerArn" in data:
        out["inference_scheduler_arn"] = data["InferenceSchedulerArn"]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    if "EventStartTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["event_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EventStartTime"]
            )
        )
    if "EventEndTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["event_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["EventEndTime"]
            )
        )
    if "Diagnostics" in data:
        out["diagnostics"] = data["Diagnostics"]
    if "EventDurationInSeconds" in data:
        out["event_duration_in_seconds"] = data["EventDurationInSeconds"]
    return out

"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AnomalyInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.timestamp
    import aws_sdk_codeguruprofiler.types.user_feedback


class AnomalyInstance(TypedDict):
    id: "str"
    """<p> The universally unique identifier (UUID) of an instance of an anomaly in a metric. </p>"""
    start_time: "aws_sdk_codeguruprofiler.types.timestamp.Timestamp"
    """<p> The start time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    end_time: NotRequired["aws_sdk_codeguruprofiler.types.timestamp.Timestamp"]
    """<p> The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>"""
    user_feedback: NotRequired[
        "aws_sdk_codeguruprofiler.types.user_feedback.UserFeedback"
    ]
    """<p>Feedback type on a specific instance of anomaly submitted by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyInstance) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_codeguruprofiler.types.timestamp

    out["startTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["endTime"] = aws_sdk_codeguruprofiler.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "user_feedback" in value:
        import aws_sdk_codeguruprofiler.types.user_feedback

        out["userFeedback"] = (
            aws_sdk_codeguruprofiler.types.user_feedback.serialize_json(
                value["user_feedback"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnomalyInstance:
    out: AnomalyInstance = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AnomalyInstance.id required")
    if "startTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["start_time"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("AnomalyInstance.start_time required")
    if "endTime" in data:
        import aws_sdk_codeguruprofiler.types.timestamp

        out["end_time"] = aws_sdk_codeguruprofiler.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "userFeedback" in data:
        import aws_sdk_codeguruprofiler.types.user_feedback

        out["user_feedback"] = (
            aws_sdk_codeguruprofiler.types.user_feedback.deserialize_json(
                data["userFeedback"]
            )
        )
    return out

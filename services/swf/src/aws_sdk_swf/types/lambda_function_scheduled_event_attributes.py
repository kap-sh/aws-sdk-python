"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionScheduledEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.duration_in_seconds_optional
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.function_id
    import aws_sdk_swf.types.function_input
    import aws_sdk_swf.types.function_name


class LambdaFunctionScheduledEventAttributes(TypedDict):
    id: "aws_sdk_swf.types.function_id.FunctionId"
    """<p>The unique ID of the Lambda task.</p>"""
    name: "aws_sdk_swf.types.function_name.FunctionName"
    """<p>The name of the Lambda function.</p>"""
    control: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>Data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the Lambda task.</p>"""
    input: NotRequired["aws_sdk_swf.types.function_input.FunctionInput"]
    """<p>The input provided to the Lambda task.</p>"""
    start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The maximum amount of time a worker can take to process the Lambda task.</p>"""
    decision_task_completed_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionCompleted</code> event corresponding to the decision that resulted in scheduling this activity task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionScheduledEventAttributes) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "control" in value:
        out["control"] = value["control"]
    if "input" in value:
        out["input"] = value["input"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionScheduledEventAttributes:
    out: LambdaFunctionScheduledEventAttributes = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("LambdaFunctionScheduledEventAttributes.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "LambdaFunctionScheduledEventAttributes.name required"
        )
    if "control" in data:
        out["control"] = data["control"]
    if "input" in data:
        out["input"] = data["input"]
    if "startToCloseTimeout" in data:
        out["start_to_close_timeout"] = data["startToCloseTimeout"]
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out

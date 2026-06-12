"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionTimedOutEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.lambda_function_timeout_type


class LambdaFunctionTimedOutEventAttributes(TypedDict):
    scheduled_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionScheduled</code> event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    started_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskStarted</code> event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    timeout_type: NotRequired[
        "aws_sdk_swf.types.lambda_function_timeout_type.LambdaFunctionTimeoutType"
    ]
    """<p>The type of the timeout that caused this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionTimedOutEventAttributes) -> dict:
    out: dict = {}
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    if "timeout_type" in value:
        import aws_sdk_swf.types.lambda_function_timeout_type

        out["timeoutType"] = (
            aws_sdk_swf.types.lambda_function_timeout_type.serialize_aws_json_1_0(
                value["timeout_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionTimedOutEventAttributes:
    out: LambdaFunctionTimedOutEventAttributes = {}  # type: ignore[typeddict-item]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if "timeoutType" in data:
        import aws_sdk_swf.types.lambda_function_timeout_type

        out["timeout_type"] = (
            aws_sdk_swf.types.lambda_function_timeout_type.deserialize_aws_json_1_0(
                data["timeoutType"]
            )
        )
    return out

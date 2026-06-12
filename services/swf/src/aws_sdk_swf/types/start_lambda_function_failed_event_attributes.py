"""Generated from Smithy shape ``com.amazonaws.swf#StartLambdaFunctionFailedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.cause_message
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.start_lambda_function_failed_cause


class StartLambdaFunctionFailedEventAttributes(TypedDict):
    scheduled_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskScheduled</code> event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    cause: NotRequired[
        "aws_sdk_swf.types.start_lambda_function_failed_cause.StartLambdaFunctionFailedCause"
    ]
    """<p>The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p> <note> <p>If <code>cause</code> is set to <code>OPERATION_NOT_PERMITTED</code>, the decision failed because the IAM role attached to the execution lacked sufficient permissions. For details and example IAM policies, see <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html\">Lambda Tasks</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""
    message: NotRequired["aws_sdk_swf.types.cause_message.CauseMessage"]
    """<p>A description that can help diagnose the cause of the fault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartLambdaFunctionFailedEventAttributes) -> dict:
    out: dict = {}
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    if "cause" in value:
        import aws_sdk_swf.types.start_lambda_function_failed_cause

        out["cause"] = (
            aws_sdk_swf.types.start_lambda_function_failed_cause.serialize_aws_json_1_0(
                value["cause"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartLambdaFunctionFailedEventAttributes:
    out: StartLambdaFunctionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "cause" in data:
        import aws_sdk_swf.types.start_lambda_function_failed_cause

        out["cause"] = (
            aws_sdk_swf.types.start_lambda_function_failed_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out

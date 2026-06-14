"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleLambdaFunctionFailedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.function_id
    import aws_sdk_swf.types.function_name
    import aws_sdk_swf.types.schedule_lambda_function_failed_cause


class ScheduleLambdaFunctionFailedEventAttributes(TypedDict):
    id: "aws_sdk_swf.types.function_id.FunctionId"
    """<p>The ID provided in the <code>ScheduleLambdaFunction</code> decision that failed. </p>"""
    name: "aws_sdk_swf.types.function_name.FunctionName"
    """<p>The name of the Lambda function.</p>"""
    cause: "aws_sdk_swf.types.schedule_lambda_function_failed_cause.ScheduleLambdaFunctionFailedCause"
    r"""<p>The cause of the failure. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p> <note> <p>If <code>cause</code> is set to <code>OPERATION_NOT_PERMITTED</code>, the decision failed because it lacked sufficient permissions. For details and example IAM policies, see <a href=\"https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html\">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>"""
    decision_task_completed_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionCompleted</code> event corresponding to the decision that resulted in scheduling this Lambda task. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleLambdaFunctionFailedEventAttributes) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_swf.types.schedule_lambda_function_failed_cause

    out["cause"] = (
        aws_sdk_swf.types.schedule_lambda_function_failed_cause.serialize_aws_json_1_0(
            value["cause"]
        )
    )
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleLambdaFunctionFailedEventAttributes:
    out: ScheduleLambdaFunctionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionFailedEventAttributes.id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionFailedEventAttributes.name required"
        )
    if "cause" in data:
        import aws_sdk_swf.types.schedule_lambda_function_failed_cause

        out["cause"] = (
            aws_sdk_swf.types.schedule_lambda_function_failed_cause.deserialize_aws_json_1_0(
                data["cause"]
            )
        )
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionFailedEventAttributes.cause required"
        )
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out

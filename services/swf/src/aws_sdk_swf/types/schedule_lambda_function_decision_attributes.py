"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleLambdaFunctionDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.duration_in_seconds_optional
    import aws_sdk_swf.types.function_id
    import aws_sdk_swf.types.function_input
    import aws_sdk_swf.types.function_name


class ScheduleLambdaFunctionDecisionAttributes(TypedDict, closed=True):
    id: "aws_sdk_swf.types.function_id.FunctionId"
    """<p>A string that identifies the Lambda function execution in the event history.</p>"""
    name: "aws_sdk_swf.types.function_name.FunctionName"
    """<p>The name, or ARN, of the Lambda function to schedule.</p>"""
    control: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The data attached to the event that the decider can use in subsequent workflow tasks. This data isn't sent to the Lambda task.</p>"""
    input: NotRequired["aws_sdk_swf.types.function_input.FunctionInput"]
    """<p>The optional input data to be supplied to the Lambda function.</p>"""
    start_to_close_timeout: NotRequired[
        "aws_sdk_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
    ]
    """<p>The timeout value, in seconds, after which the Lambda function is considered to be failed once it has started. This can be any integer from 1-900 (1s-15m).</p> <p>If no value is supplied, then a default value of 900s is assumed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleLambdaFunctionDecisionAttributes) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "control" in value:
        out["control"] = value["control"]
    if "input" in value:
        out["input"] = value["input"]
    if "start_to_close_timeout" in value:
        out["startToCloseTimeout"] = value["start_to_close_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduleLambdaFunctionDecisionAttributes:
    out: ScheduleLambdaFunctionDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionDecisionAttributes.id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "ScheduleLambdaFunctionDecisionAttributes.name required"
        )
    if "control" in data:
        out["control"] = data["control"]
    if "input" in data:
        out["input"] = data["input"]
    if "startToCloseTimeout" in data:
        out["start_to_close_timeout"] = data["startToCloseTimeout"]
    return out

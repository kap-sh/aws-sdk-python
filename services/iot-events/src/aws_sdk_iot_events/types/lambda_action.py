"""Generated from Smithy shape ``com.amazonaws.iotevents#LambdaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.payload


class LambdaAction(TypedDict, closed=True):
    function_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Lambda function that is executed.</p>"""
    payload: NotRequired["aws_sdk_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message to a Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaAction) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    if "payload" in value:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> LambdaAction:
    out: LambdaAction = {}  # type: ignore[typeddict-item]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("LambdaAction.function_arn required")
    if "payload" in data:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.deserialize_json(
            data["payload"]
        )
    return out

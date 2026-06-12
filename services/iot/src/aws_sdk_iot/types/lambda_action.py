"""Generated from Smithy shape ``com.amazonaws.iot#LambdaAction``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.function_arn


class LambdaAction(TypedDict):
    function_arn: "aws_sdk_iot.types.function_arn.FunctionArn"
    """<p>The ARN of the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaAction) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaAction:
    out: LambdaAction = {}  # type: ignore[typeddict-item]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("LambdaAction.function_arn required")
    return out

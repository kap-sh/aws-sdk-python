"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#LambdaFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.lambda_arn


class LambdaFunction(TypedDict, closed=True):
    arn: "aws_sdk_iottwinmaker.types.lambda_arn.LambdaArn"
    """<p>The ARN of the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaFunction) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaFunction:
    out: LambdaFunction = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("LambdaFunction.arn required")
    return out

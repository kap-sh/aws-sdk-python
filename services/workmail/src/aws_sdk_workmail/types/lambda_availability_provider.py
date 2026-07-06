"""Generated from Smithy shape ``com.amazonaws.workmail#LambdaAvailabilityProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.lambda_arn


class LambdaAvailabilityProvider(TypedDict, closed=True):
    lambda_arn: "aws_sdk_workmail.types.lambda_arn.LambdaArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda that acts as the availability provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaAvailabilityProvider) -> dict:
    out: dict = {}
    out["LambdaArn"] = value["lambda_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaAvailabilityProvider:
    out: LambdaAvailabilityProvider = {}  # type: ignore[typeddict-item]
    if "LambdaArn" in data:
        out["lambda_arn"] = data["LambdaArn"]
    else:
        raise DeserializationError("LambdaAvailabilityProvider.lambda_arn required")
    return out

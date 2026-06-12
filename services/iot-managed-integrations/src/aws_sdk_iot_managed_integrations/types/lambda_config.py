"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#LambdaConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.lambda_arn


class LambdaConfig(TypedDict):
    arn: "aws_sdk_iot_managed_integrations.types.lambda_arn.LambdaArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function used as an endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConfig) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaConfig:
    out: LambdaConfig = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("LambdaConfig.arn required")
    return out

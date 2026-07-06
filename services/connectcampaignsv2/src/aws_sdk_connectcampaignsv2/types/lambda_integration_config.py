"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#LambdaIntegrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.lambda_arn


class LambdaIntegrationConfig(TypedDict, closed=True):
    function_arn: "aws_sdk_connectcampaignsv2.types.lambda_arn.LambdaArn"


# --- restJson1 ser/de ---
def serialize_json(value: LambdaIntegrationConfig) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaIntegrationConfig:
    out: LambdaIntegrationConfig = {}  # type: ignore[typeddict-item]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("LambdaIntegrationConfig.function_arn required")
    return out

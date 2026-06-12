"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#LambdaIntegrationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.lambda_arn


class LambdaIntegrationSummary(TypedDict):
    function_arn: "aws_sdk_connectcampaignsv2.types.lambda_arn.LambdaArn"


# --- restJson1 ser/de ---
def serialize_json(value: LambdaIntegrationSummary) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaIntegrationSummary:
    out: LambdaIntegrationSummary = {}  # type: ignore[typeddict-item]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("LambdaIntegrationSummary.function_arn required")
    return out

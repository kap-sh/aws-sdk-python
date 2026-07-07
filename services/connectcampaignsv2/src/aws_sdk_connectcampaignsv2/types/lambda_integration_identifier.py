"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#LambdaIntegrationIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.lambda_arn


class LambdaIntegrationIdentifier(TypedDict, closed=True):
    function_arn: "aws_sdk_connectcampaignsv2.types.lambda_arn.LambdaArn"


# --- restJson1 ser/de ---
def serialize_json(value: LambdaIntegrationIdentifier) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    return out


def deserialize_json(data: dict) -> LambdaIntegrationIdentifier:
    out: LambdaIntegrationIdentifier = {}  # type: ignore[typeddict-item]
    if "functionArn" in data:
        out["function_arn"] = data["functionArn"]
    else:
        raise DeserializationError("LambdaIntegrationIdentifier.function_arn required")
    return out

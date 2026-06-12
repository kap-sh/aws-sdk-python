"""Generated from Smithy shape ``com.amazonaws.storagegateway#RetrieveTapeRecoveryPointInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.tape_arn


class RetrieveTapeRecoveryPointInput(TypedDict):
    tape_arn: "aws_sdk_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.</p>"""
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveTapeRecoveryPointInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveTapeRecoveryPointInput:
    out: RetrieveTapeRecoveryPointInput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("RetrieveTapeRecoveryPointInput.tape_arn required")
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError(
            "RetrieveTapeRecoveryPointInput.gateway_arn required"
        )
    return out

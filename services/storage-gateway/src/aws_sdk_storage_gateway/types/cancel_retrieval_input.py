"""Generated from Smithy shape ``com.amazonaws.storagegateway#CancelRetrievalInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.tape_arn


class CancelRetrievalInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    tape_arn: "aws_sdk_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelRetrievalInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["TapeARN"] = value["tape_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelRetrievalInput:
    out: CancelRetrievalInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("CancelRetrievalInput.gateway_arn required")
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("CancelRetrievalInput.tape_arn required")
    return out

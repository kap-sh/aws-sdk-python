"""Generated from Smithy shape ``com.amazonaws.storagegateway#RetrieveTapeArchiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.tape_arn


class RetrieveTapeArchiveInput(TypedDict, closed=True):
    tape_arn: "aws_sdk_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).</p>"""
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p> <p>You retrieve archived virtual tapes to only one gateway and the gateway must be a tape gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveTapeArchiveInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveTapeArchiveInput:
    out: RetrieveTapeArchiveInput = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("RetrieveTapeArchiveInput.tape_arn required")
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("RetrieveTapeArchiveInput.gateway_arn required")
    return out

"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateGatewaySoftwareNowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn


class UpdateGatewaySoftwareNowInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewaySoftwareNowInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewaySoftwareNowInput:
    out: UpdateGatewaySoftwareNowInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("UpdateGatewaySoftwareNowInput.gateway_arn required")
    return out

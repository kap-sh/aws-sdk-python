"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateGatewayInformationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.string


class UpdateGatewayInformationOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    gateway_name: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The name you configured for your gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayInformationOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "gateway_name" in value:
        out["GatewayName"] = value["gateway_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayInformationOutput:
    out: UpdateGatewayInformationOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "GatewayName" in data:
        out["gateway_name"] = data["GatewayName"]
    return out

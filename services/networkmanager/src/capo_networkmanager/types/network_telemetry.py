"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkTelemetry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_account_id
    import capo_networkmanager.types.connection_health
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.resource_arn


class NetworkTelemetry(TypedDict, closed=True):
    registered_gateway_arn: NotRequired[
        "capo_networkmanager.types.resource_arn.ResourceArn"
    ]
    """<p>The ARN of the gateway.</p>"""
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    aws_region: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Amazon Web Services Region.</p>"""
    account_id: NotRequired["capo_networkmanager.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    resource_type: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource type.</p>"""
    resource_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the resource.</p>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource.</p>"""
    address: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The address.</p>"""
    health: NotRequired["capo_networkmanager.types.connection_health.ConnectionHealth"]
    """<p>The connection health.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTelemetry) -> dict:
    out: dict = {}
    if "registered_gateway_arn" in value:
        out["RegisteredGatewayArn"] = value["registered_gateway_arn"]
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "address" in value:
        out["Address"] = value["address"]
    if "health" in value:
        import capo_networkmanager.types.connection_health

        out["Health"] = capo_networkmanager.types.connection_health.serialize_json(
            value["health"]
        )
    return out


def deserialize_json(data: dict) -> NetworkTelemetry:
    out: NetworkTelemetry = {}  # type: ignore[typeddict-item]
    if "RegisteredGatewayArn" in data:
        out["registered_gateway_arn"] = data["RegisteredGatewayArn"]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Address" in data:
        out["address"] = data["Address"]
    if "Health" in data:
        import capo_networkmanager.types.connection_health

        out["health"] = capo_networkmanager.types.connection_health.deserialize_json(
            data["Health"]
        )
    return out

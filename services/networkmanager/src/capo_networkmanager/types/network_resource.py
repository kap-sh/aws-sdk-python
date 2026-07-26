"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.aws_account_id
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.network_resource_metadata_map
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.tag_list


class NetworkResource(TypedDict, closed=True):
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
    """<p>The resource type.</p> <p>The following are the supported resource types for Direct Connect:</p> <ul> <li> <p> <code>dxcon</code> </p> </li> <li> <p> <code>dx-gateway</code> </p> </li> <li> <p> <code>dx-vif</code> </p> </li> </ul> <p>The following are the supported resource types for Network Manager:</p> <ul> <li> <p> <code>attachment</code> </p> </li> <li> <p> <code>connect-peer</code> </p> </li> <li> <p> <code>connection</code> </p> </li> <li> <p> <code>core-network</code> </p> </li> <li> <p> <code>device</code> </p> </li> <li> <p> <code>link</code> </p> </li> <li> <p> <code>peering</code> </p> </li> <li> <p> <code>site</code> </p> </li> </ul> <p>The following are the supported resource types for Amazon VPC:</p> <ul> <li> <p> <code>customer-gateway</code> </p> </li> <li> <p> <code>transit-gateway</code> </p> </li> <li> <p> <code>transit-gateway-attachment</code> </p> </li> <li> <p> <code>transit-gateway-connect-peer</code> </p> </li> <li> <p> <code>transit-gateway-route-table</code> </p> </li> <li> <p> <code>vpn-connection</code> </p> </li> </ul>"""
    resource_id: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the resource.</p>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource.</p>"""
    definition: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>Information about the resource, in JSON format. Network Manager gets this information by describing the resource using its Describe API call.</p>"""
    definition_timestamp: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The time that the resource definition was retrieved.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    metadata: NotRequired[
        "capo_networkmanager.types.network_resource_metadata_map.NetworkResourceMetadataMap"
    ]
    """<p>The resource metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkResource) -> dict:
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
    if "definition" in value:
        out["Definition"] = value["definition"]
    if "definition_timestamp" in value:
        import capo_networkmanager.types.date_time

        out["DefinitionTimestamp"] = capo_networkmanager.types.date_time.serialize_json(
            value["definition_timestamp"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "metadata" in value:
        import capo_networkmanager.types.network_resource_metadata_map

        out["Metadata"] = (
            capo_networkmanager.types.network_resource_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkResource:
    out: NetworkResource = {}  # type: ignore[typeddict-item]
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
    if "Definition" in data:
        out["definition"] = data["Definition"]
    if "DefinitionTimestamp" in data:
        import capo_networkmanager.types.date_time

        out["definition_timestamp"] = (
            capo_networkmanager.types.date_time.deserialize_json(
                data["DefinitionTimestamp"]
            )
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "Metadata" in data:
        import capo_networkmanager.types.network_resource_metadata_map

        out["metadata"] = (
            capo_networkmanager.types.network_resource_metadata_map.deserialize_json(
                data["Metadata"]
            )
        )
    return out

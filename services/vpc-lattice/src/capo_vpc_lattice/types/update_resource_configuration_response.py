"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateResourceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.boolean
    import capo_vpc_lattice.types.port_range_list
    import capo_vpc_lattice.types.protocol_type
    import capo_vpc_lattice.types.resource_configuration_arn
    import capo_vpc_lattice.types.resource_configuration_definition
    import capo_vpc_lattice.types.resource_configuration_id
    import capo_vpc_lattice.types.resource_configuration_name
    import capo_vpc_lattice.types.resource_configuration_status
    import capo_vpc_lattice.types.resource_configuration_type
    import capo_vpc_lattice.types.resource_gateway_id


class UpdateResourceConfigurationResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the resource configuration.</p>"""
    name: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName"
    ]
    """<p>The name of the resource configuration.</p>"""
    arn: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_arn.ResourceConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource configuration.</p>"""
    resource_gateway_id: NotRequired[
        "capo_vpc_lattice.types.resource_gateway_id.ResourceGatewayId"
    ]
    """<p>The ID of the resource gateway associated with the resource configuration.</p>"""
    resource_configuration_group_id: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_id.ResourceConfigurationId"
    ]
    """<p>The ID of the group resource configuration.</p>"""
    type: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType"
    ]
    """<p>The type of resource configuration.</p> <ul> <li> <p> <code>SINGLE</code> - A single resource.</p> </li> <li> <p> <code>GROUP</code> - A group of resources.</p> </li> <li> <p> <code>CHILD</code> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <code>ARN</code> - An Amazon Web Services resource.</p> </li> </ul>"""
    port_ranges: NotRequired["capo_vpc_lattice.types.port_range_list.PortRangeList"]
    """<p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>"""
    allow_association_to_shareable_service_network: NotRequired[
        "capo_vpc_lattice.types.boolean.Boolean"
    ]
    """<p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>"""
    protocol: NotRequired["capo_vpc_lattice.types.protocol_type.ProtocolType"]
    """<p>The TCP protocol accepted by the specified resource configuration.</p>"""
    status: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_status.ResourceConfigurationStatus"
    ]
    """<p>The status of the resource configuration.</p>"""
    resource_configuration_definition: NotRequired[
        "capo_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
    ]
    """<p>The resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceConfigurationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_gateway_id" in value:
        out["resourceGatewayId"] = value["resource_gateway_id"]
    if "resource_configuration_group_id" in value:
        out["resourceConfigurationGroupId"] = value["resource_configuration_group_id"]
    if "type" in value:
        import capo_vpc_lattice.types.resource_configuration_type

        out["type"] = capo_vpc_lattice.types.resource_configuration_type.serialize_json(
            value["type"]
        )
    if "port_ranges" in value:
        import capo_vpc_lattice.types.port_range_list

        out["portRanges"] = capo_vpc_lattice.types.port_range_list.serialize_json(
            value["port_ranges"]
        )
    if "allow_association_to_shareable_service_network" in value:
        out["allowAssociationToShareableServiceNetwork"] = value[
            "allow_association_to_shareable_service_network"
        ]
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "status" in value:
        out["status"] = value["status"]
    if "resource_configuration_definition" in value:
        import capo_vpc_lattice.types.resource_configuration_definition

        out["resourceConfigurationDefinition"] = (
            capo_vpc_lattice.types.resource_configuration_definition.serialize_json(
                value["resource_configuration_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResourceConfigurationResponse:
    out: UpdateResourceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceGatewayId" in data:
        out["resource_gateway_id"] = data["resourceGatewayId"]
    if "resourceConfigurationGroupId" in data:
        out["resource_configuration_group_id"] = data["resourceConfigurationGroupId"]
    if "type" in data:
        import capo_vpc_lattice.types.resource_configuration_type

        out["type"] = (
            capo_vpc_lattice.types.resource_configuration_type.deserialize_json(
                data["type"]
            )
        )
    if "portRanges" in data:
        import capo_vpc_lattice.types.port_range_list

        out["port_ranges"] = capo_vpc_lattice.types.port_range_list.deserialize_json(
            data["portRanges"]
        )
    if "allowAssociationToShareableServiceNetwork" in data:
        out["allow_association_to_shareable_service_network"] = data[
            "allowAssociationToShareableServiceNetwork"
        ]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "status" in data:
        out["status"] = data["status"]
    if "resourceConfigurationDefinition" in data:
        import capo_vpc_lattice.types.resource_configuration_definition

        out["resource_configuration_definition"] = (
            capo_vpc_lattice.types.resource_configuration_definition.deserialize_json(
                data["resourceConfigurationDefinition"]
            )
        )
    return out

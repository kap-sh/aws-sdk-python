"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateResourceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.port_range_list
    import aws_sdk_vpc_lattice.types.resource_configuration_definition
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier


class UpdateResourceConfigurationRequest(TypedDict):
    resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    """<p>The ID of the resource configuration.</p>"""
    resource_configuration_definition: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
    ]
    """<p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>"""
    allow_association_to_shareable_service_network: NotRequired[
        "aws_sdk_vpc_lattice.types.boolean.Boolean"
    ]
    """<p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>"""
    port_ranges: NotRequired["aws_sdk_vpc_lattice.types.port_range_list.PortRangeList"]
    """<p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceConfigurationRequest) -> dict:
    out: dict = {}
    if "resource_configuration_definition" in value:
        import aws_sdk_vpc_lattice.types.resource_configuration_definition

        out["resourceConfigurationDefinition"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_definition.serialize_json(
                value["resource_configuration_definition"]
            )
        )
    if "allow_association_to_shareable_service_network" in value:
        out["allowAssociationToShareableServiceNetwork"] = value[
            "allow_association_to_shareable_service_network"
        ]
    if "port_ranges" in value:
        import aws_sdk_vpc_lattice.types.port_range_list

        out["portRanges"] = aws_sdk_vpc_lattice.types.port_range_list.serialize_json(
            value["port_ranges"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResourceConfigurationRequest:
    out: UpdateResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "resourceConfigurationDefinition" in data:
        import aws_sdk_vpc_lattice.types.resource_configuration_definition

        out["resource_configuration_definition"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_definition.deserialize_json(
                data["resourceConfigurationDefinition"]
            )
        )
    if "allowAssociationToShareableServiceNetwork" in data:
        out["allow_association_to_shareable_service_network"] = data[
            "allowAssociationToShareableServiceNetwork"
        ]
    if "portRanges" in data:
        import aws_sdk_vpc_lattice.types.port_range_list

        out["port_ranges"] = aws_sdk_vpc_lattice.types.port_range_list.deserialize_json(
            data["portRanges"]
        )
    return out

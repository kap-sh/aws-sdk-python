"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceConfigurationDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.arn_resource
    import aws_sdk_vpc_lattice.types.dns_resource
    import aws_sdk_vpc_lattice.types.ip_resource


class _ResourceConfigurationDefinition_dnsResource(TypedDict, closed=True):
    dnsResource: "aws_sdk_vpc_lattice.types.dns_resource.DnsResource"


class _ResourceConfigurationDefinition_ipResource(TypedDict, closed=True):
    ipResource: "aws_sdk_vpc_lattice.types.ip_resource.IpResource"


class _ResourceConfigurationDefinition_arnResource(TypedDict, closed=True):
    arnResource: "aws_sdk_vpc_lattice.types.arn_resource.ArnResource"


ResourceConfigurationDefinition: TypeAlias = (
    _ResourceConfigurationDefinition_dnsResource
    | _ResourceConfigurationDefinition_ipResource
    | _ResourceConfigurationDefinition_arnResource
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurationDefinition) -> dict:
    if "dnsResource" in value:
        import aws_sdk_vpc_lattice.types.dns_resource

        return {
            "dnsResource": aws_sdk_vpc_lattice.types.dns_resource.serialize_json(
                value["dnsResource"]
            )
        }
    elif "ipResource" in value:
        import aws_sdk_vpc_lattice.types.ip_resource

        return {
            "ipResource": aws_sdk_vpc_lattice.types.ip_resource.serialize_json(
                value["ipResource"]
            )
        }
    elif "arnResource" in value:
        import aws_sdk_vpc_lattice.types.arn_resource

        return {
            "arnResource": aws_sdk_vpc_lattice.types.arn_resource.serialize_json(
                value["arnResource"]
            )
        }
    else:
        raise SerializationError("ResourceConfigurationDefinition: no variant present")


def deserialize_json(data: dict) -> ResourceConfigurationDefinition:
    if "dnsResource" in data:
        import aws_sdk_vpc_lattice.types.dns_resource

        return {
            "dnsResource": aws_sdk_vpc_lattice.types.dns_resource.deserialize_json(
                data["dnsResource"]
            )
        }
    elif "ipResource" in data:
        import aws_sdk_vpc_lattice.types.ip_resource

        return {
            "ipResource": aws_sdk_vpc_lattice.types.ip_resource.deserialize_json(
                data["ipResource"]
            )
        }
    elif "arnResource" in data:
        import aws_sdk_vpc_lattice.types.arn_resource

        return {
            "arnResource": aws_sdk_vpc_lattice.types.arn_resource.deserialize_json(
                data["arnResource"]
            )
        }
    else:
        raise DeserializationError(
            "ResourceConfigurationDefinition: no recognized variant key"
        )

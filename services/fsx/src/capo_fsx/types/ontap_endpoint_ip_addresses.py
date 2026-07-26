"""Generated from Smithy shape ``com.amazonaws.fsx#OntapEndpointIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.ip_address

OntapEndpointIpAddresses: TypeAlias = list["capo_fsx.types.ip_address.IpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapEndpointIpAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OntapEndpointIpAddresses:
    return list(data)

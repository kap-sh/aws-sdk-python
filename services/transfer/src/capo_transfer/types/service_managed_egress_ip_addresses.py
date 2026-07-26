"""Generated from Smithy shape ``com.amazonaws.transfer#ServiceManagedEgressIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.service_managed_egress_ip_address

ServiceManagedEgressIpAddresses: TypeAlias = list[
    "capo_transfer.types.service_managed_egress_ip_address.ServiceManagedEgressIpAddress"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceManagedEgressIpAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ServiceManagedEgressIpAddresses:
    return list(data)

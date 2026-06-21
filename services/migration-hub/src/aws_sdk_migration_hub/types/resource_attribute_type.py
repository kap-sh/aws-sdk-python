"""Generated from Smithy shape ``com.amazonaws.migrationhub#ResourceAttributeType``."""

from typing import Literal, TypeAlias, cast

ResourceAttributeType: TypeAlias = Literal[
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "MAC_ADDRESS",
    "FQDN",
    "VM_MANAGER_ID",
    "VM_MANAGED_OBJECT_REFERENCE",
    "VM_NAME",
    "VM_PATH",
    "BIOS_ID",
    "MOTHERBOARD_SERIAL_NUMBER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceAttributeType:
    return cast(ResourceAttributeType, data)

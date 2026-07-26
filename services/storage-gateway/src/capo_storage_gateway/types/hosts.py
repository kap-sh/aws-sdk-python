"""Generated from Smithy shape ``com.amazonaws.storagegateway#Hosts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.host

Hosts: TypeAlias = list["capo_storage_gateway.types.host.Host"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Hosts) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Hosts:
    return list(data)

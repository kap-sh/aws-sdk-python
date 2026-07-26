"""Generated from Smithy shape ``com.amazonaws.inspector#Ipv6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.text

Ipv6Addresses: TypeAlias = list["capo_inspector.types.text.Text"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ipv6Addresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Ipv6Addresses:
    return list(data)

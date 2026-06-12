"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProtocolNumbers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.protocol_number

ProtocolNumbers: TypeAlias = list[
    "aws_sdk_network_firewall.types.protocol_number.ProtocolNumber"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProtocolNumbers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProtocolNumbers:
    return list(data)

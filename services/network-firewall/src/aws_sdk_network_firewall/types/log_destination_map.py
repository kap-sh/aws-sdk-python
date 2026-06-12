"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogDestinationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.hash_map_key
    import aws_sdk_network_firewall.types.hash_map_value

LogDestinationMap: TypeAlias = dict[
    "aws_sdk_network_firewall.types.hash_map_key.HashMapKey",
    "aws_sdk_network_firewall.types.hash_map_value.HashMapValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: LogDestinationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDestinationMap:
    out: LogDestinationMap = {}
    for key, value in data.items():
        out[key] = value
    return out

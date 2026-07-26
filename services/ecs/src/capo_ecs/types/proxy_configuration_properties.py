"""Generated from Smithy shape ``com.amazonaws.ecs#ProxyConfigurationProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.key_value_pair

ProxyConfigurationProperties: TypeAlias = list[
    "capo_ecs.types.key_value_pair.KeyValuePair"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfigurationProperties) -> list:
    import capo_ecs.types.key_value_pair

    out: list = []
    for item in value:
        out.append(capo_ecs.types.key_value_pair.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProxyConfigurationProperties:
    import capo_ecs.types.key_value_pair

    out: ProxyConfigurationProperties = []
    for item in data:
        out.append(capo_ecs.types.key_value_pair.deserialize_aws_json_1_1(item))
    return out

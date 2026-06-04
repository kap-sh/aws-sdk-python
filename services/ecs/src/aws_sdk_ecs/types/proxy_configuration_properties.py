"""Generated from Smithy shape ``com.amazonaws.ecs#ProxyConfigurationProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.key_value_pair

ProxyConfigurationProperties: TypeAlias = list[
    "aws_sdk_ecs.types.key_value_pair.KeyValuePair"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProxyConfigurationProperties) -> list:
    import aws_sdk_ecs.types.key_value_pair

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.key_value_pair.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProxyConfigurationProperties:
    import aws_sdk_ecs.types.key_value_pair

    out: ProxyConfigurationProperties = []
    for item in data:
        out.append(aws_sdk_ecs.types.key_value_pair.deserialize_aws_json_1_1(item))
    return out

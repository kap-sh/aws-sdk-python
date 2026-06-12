"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfVpcConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.vpc_config

__listOfVpcConfig: TypeAlias = list["aws_sdk_kafka.types.vpc_config.VpcConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcConfig) -> list:
    import aws_sdk_kafka.types.vpc_config

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.vpc_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVpcConfig:
    import aws_sdk_kafka.types.vpc_config

    out: __listOfVpcConfig = []
    for item in data:
        out.append(aws_sdk_kafka.types.vpc_config.deserialize_json(item))
    return out

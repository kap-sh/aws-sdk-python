"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfVpcConnection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.vpc_connection

__listOfVpcConnection: TypeAlias = list[
    "aws_sdk_kafka.types.vpc_connection.VpcConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcConnection) -> list:
    import aws_sdk_kafka.types.vpc_connection

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.vpc_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVpcConnection:
    import aws_sdk_kafka.types.vpc_connection

    out: __listOfVpcConnection = []
    for item in data:
        out.append(aws_sdk_kafka.types.vpc_connection.deserialize_json(item))
    return out

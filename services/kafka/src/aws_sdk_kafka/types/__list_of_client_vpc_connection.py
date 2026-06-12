"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfClientVpcConnection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.client_vpc_connection

__listOfClientVpcConnection: TypeAlias = list[
    "aws_sdk_kafka.types.client_vpc_connection.ClientVpcConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClientVpcConnection) -> list:
    import aws_sdk_kafka.types.client_vpc_connection

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.client_vpc_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfClientVpcConnection:
    import aws_sdk_kafka.types.client_vpc_connection

    out: __listOfClientVpcConnection = []
    for item in data:
        out.append(aws_sdk_kafka.types.client_vpc_connection.deserialize_json(item))
    return out

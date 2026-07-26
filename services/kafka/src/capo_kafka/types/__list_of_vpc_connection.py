"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfVpcConnection``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.vpc_connection

__listOfVpcConnection: TypeAlias = list["capo_kafka.types.vpc_connection.VpcConnection"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVpcConnection) -> list:
    import capo_kafka.types.vpc_connection

    out: list = []
    for item in value:
        out.append(capo_kafka.types.vpc_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVpcConnection:
    import capo_kafka.types.vpc_connection

    out: __listOfVpcConnection = []
    for item in data:
        out.append(capo_kafka.types.vpc_connection.deserialize_json(item))
    return out

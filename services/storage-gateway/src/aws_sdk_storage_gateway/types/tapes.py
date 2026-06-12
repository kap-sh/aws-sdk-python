"""Generated from Smithy shape ``com.amazonaws.storagegateway#Tapes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape

Tapes: TypeAlias = list["aws_sdk_storage_gateway.types.tape.Tape"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tapes) -> list:
    import aws_sdk_storage_gateway.types.tape

    out: list = []
    for item in value:
        out.append(aws_sdk_storage_gateway.types.tape.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Tapes:
    import aws_sdk_storage_gateway.types.tape

    out: Tapes = []
    for item in data:
        out.append(aws_sdk_storage_gateway.types.tape.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape_arn

TapeARNs: TypeAlias = list["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeARNs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TapeARNs:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#Operations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.operation

Operations: TypeAlias = list["aws_sdk_cloudcontrol.types.operation.Operation"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Operations) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Operations:
    return list(data)

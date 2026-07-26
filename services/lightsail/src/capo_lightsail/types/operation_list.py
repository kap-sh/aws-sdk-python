"""Generated from Smithy shape ``com.amazonaws.lightsail#OperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.operation

OperationList: TypeAlias = list["capo_lightsail.types.operation.Operation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationList) -> list:
    import capo_lightsail.types.operation

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.operation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OperationList:
    import capo_lightsail.types.operation

    out: OperationList = []
    for item in data:
        out.append(capo_lightsail.types.operation.deserialize_aws_json_1_1(item))
    return out

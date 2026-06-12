"""Generated from Smithy shape ``com.amazonaws.rdsdata#ArrayValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.value

ArrayValueList: TypeAlias = list["aws_sdk_rds_data.types.value.Value"]


# --- restJson1 ser/de ---
def serialize_json(value: ArrayValueList) -> list:
    import aws_sdk_rds_data.types.value

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.value.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArrayValueList:
    import aws_sdk_rds_data.types.value

    out: ArrayValueList = []
    for item in data:
        out.append(aws_sdk_rds_data.types.value.deserialize_json(item))
    return out

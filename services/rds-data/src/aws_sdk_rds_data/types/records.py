"""Generated from Smithy shape ``com.amazonaws.rdsdata#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.record

Records: TypeAlias = list["aws_sdk_rds_data.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: Records) -> list:
    import aws_sdk_rds_data.types.record

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> Records:
    import aws_sdk_rds_data.types.record

    out: Records = []
    for item in data:
        out.append(aws_sdk_rds_data.types.record.deserialize_json(item))
    return out

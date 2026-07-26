"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DatabaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_write.types.database

DatabaseList: TypeAlias = list["capo_timestream_write.types.database.Database"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseList) -> list:
    import capo_timestream_write.types.database

    out: list = []
    for item in value:
        out.append(capo_timestream_write.types.database.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DatabaseList:
    import capo_timestream_write.types.database

    out: DatabaseList = []
    for item in data:
        out.append(capo_timestream_write.types.database.deserialize_aws_json_1_0(item))
    return out

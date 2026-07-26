"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Records``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_write.types.record

Records: TypeAlias = list["capo_timestream_write.types.record.Record"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Records) -> list:
    import capo_timestream_write.types.record

    out: list = []
    for item in value:
        out.append(capo_timestream_write.types.record.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Records:
    import capo_timestream_write.types.record

    out: Records = []
    for item in data:
        out.append(capo_timestream_write.types.record.deserialize_aws_json_1_0(item))
    return out

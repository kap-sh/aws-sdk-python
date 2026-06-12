"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#RejectedRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.rejected_record

RejectedRecords: TypeAlias = list[
    "aws_sdk_timestream_write.types.rejected_record.RejectedRecord"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectedRecords) -> list:
    import aws_sdk_timestream_write.types.rejected_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_write.types.rejected_record.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RejectedRecords:
    import aws_sdk_timestream_write.types.rejected_record

    out: RejectedRecords = []
    for item in data:
        out.append(
            aws_sdk_timestream_write.types.rejected_record.deserialize_aws_json_1_0(
                item
            )
        )
    return out

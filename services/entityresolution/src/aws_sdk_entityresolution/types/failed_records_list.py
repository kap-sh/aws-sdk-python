"""Generated from Smithy shape ``com.amazonaws.entityresolution#FailedRecordsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.failed_record

FailedRecordsList: TypeAlias = list[
    "aws_sdk_entityresolution.types.failed_record.FailedRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedRecordsList) -> list:
    import aws_sdk_entityresolution.types.failed_record

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.failed_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedRecordsList:
    import aws_sdk_entityresolution.types.failed_record

    out: FailedRecordsList = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.failed_record.deserialize_json(item))
    return out

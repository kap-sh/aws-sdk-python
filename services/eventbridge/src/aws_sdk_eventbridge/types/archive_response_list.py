"""Generated from Smithy shape ``com.amazonaws.eventbridge#ArchiveResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.archive

ArchiveResponseList: TypeAlias = list["aws_sdk_eventbridge.types.archive.Archive"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArchiveResponseList) -> list:
    import aws_sdk_eventbridge.types.archive

    out: list = []
    for item in value:
        out.append(aws_sdk_eventbridge.types.archive.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ArchiveResponseList:
    import aws_sdk_eventbridge.types.archive

    out: ArchiveResponseList = []
    for item in data:
        out.append(aws_sdk_eventbridge.types.archive.deserialize_aws_json_1_1(item))
    return out

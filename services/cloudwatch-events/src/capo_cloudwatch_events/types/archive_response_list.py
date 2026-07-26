"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ArchiveResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.archive

ArchiveResponseList: TypeAlias = list["capo_cloudwatch_events.types.archive.Archive"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArchiveResponseList) -> list:
    import capo_cloudwatch_events.types.archive

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_events.types.archive.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ArchiveResponseList:
    import capo_cloudwatch_events.types.archive

    out: ArchiveResponseList = []
    for item in data:
        out.append(capo_cloudwatch_events.types.archive.deserialize_aws_json_1_1(item))
    return out

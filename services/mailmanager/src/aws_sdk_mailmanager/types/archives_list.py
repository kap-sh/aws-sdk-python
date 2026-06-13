"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchivesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive

ArchivesList: TypeAlias = list["aws_sdk_mailmanager.types.archive.Archive"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchivesList) -> list:
    import aws_sdk_mailmanager.types.archive

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.archive.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ArchivesList:
    import aws_sdk_mailmanager.types.archive

    out: ArchivesList = []
    for item in data:
        out.append(aws_sdk_mailmanager.types.archive.deserialize_aws_json_1_0(item))
    return out

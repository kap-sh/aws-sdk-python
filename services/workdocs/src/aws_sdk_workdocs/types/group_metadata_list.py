"""Generated from Smithy shape ``com.amazonaws.workdocs#GroupMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.group_metadata

GroupMetadataList: TypeAlias = list[
    "aws_sdk_workdocs.types.group_metadata.GroupMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupMetadataList) -> list:
    import aws_sdk_workdocs.types.group_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.group_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupMetadataList:
    import aws_sdk_workdocs.types.group_metadata

    out: GroupMetadataList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.group_metadata.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.workdocs#UserMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.user_metadata

UserMetadataList: TypeAlias = list["aws_sdk_workdocs.types.user_metadata.UserMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: UserMetadataList) -> list:
    import aws_sdk_workdocs.types.user_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.user_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserMetadataList:
    import aws_sdk_workdocs.types.user_metadata

    out: UserMetadataList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.user_metadata.deserialize_json(item))
    return out

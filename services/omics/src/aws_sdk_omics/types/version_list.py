"""Generated from Smithy shape ``com.amazonaws.omics#VersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.version_name

VersionList: TypeAlias = list["aws_sdk_omics.types.version_name.VersionName"]


# --- restJson1 ser/de ---
def serialize_json(value: VersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> VersionList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.outposts#SupportedStorageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.supported_storage_enum

SupportedStorageList: TypeAlias = list[
    "aws_sdk_outposts.types.supported_storage_enum.SupportedStorageEnum"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedStorageList) -> list:
    import aws_sdk_outposts.types.supported_storage_enum

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.supported_storage_enum.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedStorageList:
    import aws_sdk_outposts.types.supported_storage_enum

    out: SupportedStorageList = []
    for item in data:
        out.append(aws_sdk_outposts.types.supported_storage_enum.deserialize_json(item))
    return out

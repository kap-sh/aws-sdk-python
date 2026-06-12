"""Generated from Smithy shape ``com.amazonaws.securityhub#MetadataUidList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string

MetadataUidList: TypeAlias = list[
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataUidList) -> list:
    return list(value)


def deserialize_json(data: list) -> MetadataUidList:
    return list(data)

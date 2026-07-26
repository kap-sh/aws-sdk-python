"""Generated from Smithy shape ``com.amazonaws.pricing#FileFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pricing.types.file_format

FileFormats: TypeAlias = list["capo_pricing.types.file_format.FileFormat"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileFormats) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileFormats:
    return list(data)

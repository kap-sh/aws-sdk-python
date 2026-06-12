"""Generated from Smithy shape ``com.amazonaws.transfer#HomeDirectoryMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.home_directory_map_entry

HomeDirectoryMappings: TypeAlias = list[
    "aws_sdk_transfer.types.home_directory_map_entry.HomeDirectoryMapEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeDirectoryMappings) -> list:
    import aws_sdk_transfer.types.home_directory_map_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transfer.types.home_directory_map_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HomeDirectoryMappings:
    import aws_sdk_transfer.types.home_directory_map_entry

    out: HomeDirectoryMappings = []
    for item in data:
        out.append(
            aws_sdk_transfer.types.home_directory_map_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out

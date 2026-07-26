"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.file_system

FileSystems: TypeAlias = list["capo_fsx.types.file_system.FileSystem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystems) -> list:
    import capo_fsx.types.file_system

    out: list = []
    for item in value:
        out.append(capo_fsx.types.file_system.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FileSystems:
    import capo_fsx.types.file_system

    out: FileSystems = []
    for item in data:
        out.append(capo_fsx.types.file_system.deserialize_aws_json_1_1(item))
    return out

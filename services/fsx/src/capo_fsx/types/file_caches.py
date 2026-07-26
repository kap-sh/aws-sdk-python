"""Generated from Smithy shape ``com.amazonaws.fsx#FileCaches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.file_cache

FileCaches: TypeAlias = list["capo_fsx.types.file_cache.FileCache"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCaches) -> list:
    import capo_fsx.types.file_cache

    out: list = []
    for item in value:
        out.append(capo_fsx.types.file_cache.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FileCaches:
    import capo_fsx.types.file_cache

    out: FileCaches = []
    for item in data:
        out.append(capo_fsx.types.file_cache.deserialize_aws_json_1_1(item))
    return out

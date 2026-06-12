"""Generated from Smithy shape ``com.amazonaws.fsx#FileCaches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache

FileCaches: TypeAlias = list["aws_sdk_fsx.types.file_cache.FileCache"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCaches) -> list:
    import aws_sdk_fsx.types.file_cache

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.file_cache.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FileCaches:
    import aws_sdk_fsx.types.file_cache

    out: FileCaches = []
    for item in data:
        out.append(aws_sdk_fsx.types.file_cache.deserialize_aws_json_1_1(item))
    return out

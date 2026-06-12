"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.file_cache_id

FileCacheIds: TypeAlias = list["aws_sdk_fsx.types.file_cache_id.FileCacheId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FileCacheIds:
    return list(data)

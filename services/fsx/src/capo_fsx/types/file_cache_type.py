"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheType``."""

from typing import Literal, TypeAlias, cast

FileCacheType: TypeAlias = Literal["LUSTRE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileCacheType:
    return cast(FileCacheType, data)

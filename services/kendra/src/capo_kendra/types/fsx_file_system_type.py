"""Generated from Smithy shape ``com.amazonaws.kendra#FsxFileSystemType``."""

from typing import Literal, TypeAlias, cast

FsxFileSystemType: TypeAlias = Literal["WINDOWS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxFileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FsxFileSystemType:
    return cast(FsxFileSystemType, data)

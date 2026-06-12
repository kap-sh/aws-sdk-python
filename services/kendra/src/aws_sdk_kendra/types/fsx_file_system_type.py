"""Generated from Smithy shape ``com.amazonaws.kendra#FsxFileSystemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

FsxFileSystemType: TypeAlias = Literal["WINDOWS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WINDOWS",))


def serialize_aws_json_1_1(value: FsxFileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FsxFileSystemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FsxFileSystemType value: {data!r}")
    return cast(FsxFileSystemType, data)

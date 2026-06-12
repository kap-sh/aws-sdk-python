"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSFileSystemUserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OpenZFSFileSystemUserType: TypeAlias = Literal["POSIX",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("POSIX",))


def serialize_aws_json_1_1(value: OpenZFSFileSystemUserType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSFileSystemUserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenZFSFileSystemUserType value: {data!r}")
    return cast(OpenZFSFileSystemUserType, data)

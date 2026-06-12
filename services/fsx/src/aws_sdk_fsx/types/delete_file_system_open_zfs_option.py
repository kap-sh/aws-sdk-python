"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemOpenZFSOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DeleteFileSystemOpenZFSOption: TypeAlias = Literal[
    "DELETE_CHILD_VOLUMES_AND_SNAPSHOTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DELETE_CHILD_VOLUMES_AND_SNAPSHOTS",))


def serialize_aws_json_1_1(value: DeleteFileSystemOpenZFSOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteFileSystemOpenZFSOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeleteFileSystemOpenZFSOption value: {data!r}"
        )
    return cast(DeleteFileSystemOpenZFSOption, data)

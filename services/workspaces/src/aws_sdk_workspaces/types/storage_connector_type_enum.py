"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnectorTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

StorageConnectorTypeEnum: TypeAlias = Literal["HOME_FOLDER",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HOME_FOLDER",))


def serialize_aws_json_1_1(value: StorageConnectorTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageConnectorTypeEnum value: {data!r}")
    return cast(StorageConnectorTypeEnum, data)

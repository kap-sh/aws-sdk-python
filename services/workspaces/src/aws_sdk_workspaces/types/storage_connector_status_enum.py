"""Generated from Smithy shape ``com.amazonaws.workspaces#StorageConnectorStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

StorageConnectorStatusEnum: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: StorageConnectorStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageConnectorStatusEnum value: {data!r}"
        )
    return cast(StorageConnectorStatusEnum, data)

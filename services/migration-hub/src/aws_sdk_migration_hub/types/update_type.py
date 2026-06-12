"""Generated from Smithy shape ``com.amazonaws.migrationhub#UpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_migration_hub.errors import DeserializationError

UpdateType: TypeAlias = Literal["MIGRATION_TASK_STATE_UPDATED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MIGRATION_TASK_STATE_UPDATED",))


def serialize_aws_json_1_1(value: UpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateType value: {data!r}")
    return cast(UpdateType, data)

"""Generated from Smithy shape ``com.amazonaws.migrationhub#UpdateType``."""

from typing import Literal, TypeAlias, cast

UpdateType: TypeAlias = Literal["MIGRATION_TASK_STATE_UPDATED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateType:
    return cast(UpdateType, data)

"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationRestoreType``."""

from typing import Literal, TypeAlias, cast

ApplicationRestoreType: TypeAlias = Literal[
    "SKIP_RESTORE_FROM_SNAPSHOT",
    "RESTORE_FROM_LATEST_SNAPSHOT",
    "RESTORE_FROM_CUSTOM_SNAPSHOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationRestoreType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationRestoreType:
    return cast(ApplicationRestoreType, data)

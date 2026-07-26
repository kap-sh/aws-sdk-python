"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#VersionStatus``."""

from typing import Literal, TypeAlias, cast

VersionStatus: TypeAlias = Literal[
    "UP_TO_DATE",
    "OUTDATED",
    "UNSUPPORTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VersionStatus:
    return cast(VersionStatus, data)

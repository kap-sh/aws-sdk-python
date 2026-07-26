"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorStatus``."""

from typing import Literal, TypeAlias, cast

CollectorStatus: TypeAlias = Literal[
    "UNREGISTERED",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CollectorStatus:
    return cast(CollectorStatus, data)

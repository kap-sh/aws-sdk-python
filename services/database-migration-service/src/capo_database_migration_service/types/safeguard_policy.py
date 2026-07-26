"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SafeguardPolicy``."""

from typing import Literal, TypeAlias, cast

SafeguardPolicy: TypeAlias = Literal[
    "rely-on-sql-server-replication-agent",
    "exclusive-automatic-truncation",
    "shared-automatic-truncation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SafeguardPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SafeguardPolicy:
    return cast(SafeguardPolicy, data)

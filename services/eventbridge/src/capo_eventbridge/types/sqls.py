"""Generated from Smithy shape ``com.amazonaws.eventbridge#Sqls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.sql

Sqls: TypeAlias = list["capo_eventbridge.types.sql.Sql"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sqls) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Sqls:
    return list(data)

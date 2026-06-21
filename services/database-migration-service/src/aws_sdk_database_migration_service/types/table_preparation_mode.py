"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TablePreparationMode``."""

from typing import Literal, TypeAlias, cast

TablePreparationMode: TypeAlias = Literal[
    "do-nothing",
    "truncate",
    "drop-tables-on-target",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TablePreparationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TablePreparationMode:
    return cast(TablePreparationMode, data)

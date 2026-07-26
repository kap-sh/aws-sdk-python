"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerType``."""

from typing import Literal, TypeAlias, cast

TableOptimizerType: TypeAlias = Literal[
    "compaction",
    "retention",
    "orphan_file_deletion",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableOptimizerType:
    return cast(TableOptimizerType, data)

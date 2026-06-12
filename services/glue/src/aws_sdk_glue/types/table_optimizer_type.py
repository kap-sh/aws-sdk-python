"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TableOptimizerType: TypeAlias = Literal[
    "compaction",
    "retention",
    "orphan_file_deletion",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "compaction",
        "retention",
        "orphan_file_deletion",
    )
)


def serialize_aws_json_1_1(value: TableOptimizerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableOptimizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableOptimizerType value: {data!r}")
    return cast(TableOptimizerType, data)

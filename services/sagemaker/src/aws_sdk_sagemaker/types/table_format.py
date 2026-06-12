"""Generated from Smithy shape ``com.amazonaws.sagemaker#TableFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TableFormat: TypeAlias = Literal[
    "Default",
    "Glue",
    "Iceberg",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Default",
        "Glue",
        "Iceberg",
    )
)


def serialize_aws_json_1_1(value: TableFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableFormat value: {data!r}")
    return cast(TableFormat, data)

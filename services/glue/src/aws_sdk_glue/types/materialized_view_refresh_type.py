"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

MaterializedViewRefreshType: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "INCREMENTAL",
    )
)


def serialize_aws_json_1_1(value: MaterializedViewRefreshType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaterializedViewRefreshType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MaterializedViewRefreshType value: {data!r}"
        )
    return cast(MaterializedViewRefreshType, data)

"""Generated from Smithy shape ``com.amazonaws.glue#ViewDialect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ViewDialect: TypeAlias = Literal[
    "REDSHIFT",
    "ATHENA",
    "SPARK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REDSHIFT",
        "ATHENA",
        "SPARK",
    )
)


def serialize_aws_json_1_1(value: ViewDialect) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ViewDialect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ViewDialect value: {data!r}")
    return cast(ViewDialect, data)

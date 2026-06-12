"""Generated from Smithy shape ``com.amazonaws.athena#StatementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

StatementType: TypeAlias = Literal[
    "DDL",
    "DML",
    "UTILITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DDL",
        "DML",
        "UTILITY",
    )
)


def serialize_aws_json_1_1(value: StatementType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatementType value: {data!r}")
    return cast(StatementType, data)

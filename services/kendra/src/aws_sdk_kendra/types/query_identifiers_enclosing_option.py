"""Generated from Smithy shape ``com.amazonaws.kendra#QueryIdentifiersEnclosingOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

QueryIdentifiersEnclosingOption: TypeAlias = Literal[
    "DOUBLE_QUOTES",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOUBLE_QUOTES",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: QueryIdentifiersEnclosingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryIdentifiersEnclosingOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QueryIdentifiersEnclosingOption value: {data!r}"
        )
    return cast(QueryIdentifiersEnclosingOption, data)

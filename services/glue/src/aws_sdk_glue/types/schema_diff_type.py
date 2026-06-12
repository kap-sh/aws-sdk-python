"""Generated from Smithy shape ``com.amazonaws.glue#SchemaDiffType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SchemaDiffType: TypeAlias = Literal["SYNTAX_DIFF",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SYNTAX_DIFF",))


def serialize_aws_json_1_1(value: SchemaDiffType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaDiffType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaDiffType value: {data!r}")
    return cast(SchemaDiffType, data)

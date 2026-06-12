"""Generated from Smithy shape ``com.amazonaws.kendra#WarningCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

WarningCode: TypeAlias = Literal["QUERY_LANGUAGE_INVALID_SYNTAX",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("QUERY_LANGUAGE_INVALID_SYNTAX",))


def serialize_aws_json_1_1(value: WarningCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WarningCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WarningCode value: {data!r}")
    return cast(WarningCode, data)

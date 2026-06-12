"""Generated from Smithy shape ``com.amazonaws.inspector#Locale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

Locale: TypeAlias = Literal["EN_US",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EN_US",))


def serialize_aws_json_1_1(value: Locale) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Locale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Locale value: {data!r}")
    return cast(Locale, data)

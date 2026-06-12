"""Generated from Smithy shape ``com.amazonaws.translate#Brevity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

Brevity: TypeAlias = Literal["ON",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ON",))


def serialize_aws_json_1_1(value: Brevity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Brevity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Brevity value: {data!r}")
    return cast(Brevity, data)

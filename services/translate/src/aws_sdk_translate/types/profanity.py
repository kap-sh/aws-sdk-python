"""Generated from Smithy shape ``com.amazonaws.translate#Profanity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

Profanity: TypeAlias = Literal["MASK",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MASK",))


def serialize_aws_json_1_1(value: Profanity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Profanity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Profanity value: {data!r}")
    return cast(Profanity, data)

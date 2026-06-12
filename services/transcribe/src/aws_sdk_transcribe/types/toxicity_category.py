"""Generated from Smithy shape ``com.amazonaws.transcribe#ToxicityCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

ToxicityCategory: TypeAlias = Literal["ALL",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_aws_json_1_1(value: ToxicityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ToxicityCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ToxicityCategory value: {data!r}")
    return cast(ToxicityCategory, data)

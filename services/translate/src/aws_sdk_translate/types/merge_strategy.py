"""Generated from Smithy shape ``com.amazonaws.translate#MergeStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_translate.errors import DeserializationError

MergeStrategy: TypeAlias = Literal["OVERWRITE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OVERWRITE",))


def serialize_aws_json_1_1(value: MergeStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MergeStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MergeStrategy value: {data!r}")
    return cast(MergeStrategy, data)

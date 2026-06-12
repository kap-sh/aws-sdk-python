"""Generated from Smithy shape ``com.amazonaws.codepipeline#BlockerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

BlockerType: TypeAlias = Literal["Schedule",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Schedule",))


def serialize_aws_json_1_1(value: BlockerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockerType value: {data!r}")
    return cast(BlockerType, data)

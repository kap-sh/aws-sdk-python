"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

TargetFilterName: TypeAlias = Literal["TARGET_STATUS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TARGET_STATUS",))


def serialize_aws_json_1_1(value: TargetFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetFilterName value: {data!r}")
    return cast(TargetFilterName, data)

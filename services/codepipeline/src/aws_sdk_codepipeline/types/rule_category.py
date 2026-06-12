"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

RuleCategory: TypeAlias = Literal["Rule",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Rule",))


def serialize_aws_json_1_1(value: RuleCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleCategory value: {data!r}")
    return cast(RuleCategory, data)

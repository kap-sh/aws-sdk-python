"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleOwner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

RuleOwner: TypeAlias = Literal["AWS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS",))


def serialize_aws_json_1_1(value: RuleOwner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleOwner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleOwner value: {data!r}")
    return cast(RuleOwner, data)

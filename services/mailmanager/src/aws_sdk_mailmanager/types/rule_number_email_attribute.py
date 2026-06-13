"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleNumberEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleNumberEmailAttribute: TypeAlias = Literal["MESSAGE_SIZE",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("MESSAGE_SIZE",))


def serialize_aws_json_1_0(value: RuleNumberEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleNumberEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleNumberEmailAttribute value: {data!r}")
    return cast(RuleNumberEmailAttribute, data)

"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleIpEmailAttribute: TypeAlias = Literal["SOURCE_IP",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SOURCE_IP",))


def serialize_aws_json_1_0(value: RuleIpEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleIpEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleIpEmailAttribute value: {data!r}")
    return cast(RuleIpEmailAttribute, data)

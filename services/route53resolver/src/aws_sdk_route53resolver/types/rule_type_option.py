"""Generated from Smithy shape ``com.amazonaws.route53resolver#RuleTypeOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

RuleTypeOption: TypeAlias = Literal[
    "FORWARD",
    "SYSTEM",
    "RECURSIVE",
    "DELEGATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FORWARD",
        "SYSTEM",
        "RECURSIVE",
        "DELEGATE",
    )
)


def serialize_aws_json_1_1(value: RuleTypeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleTypeOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleTypeOption value: {data!r}")
    return cast(RuleTypeOption, data)

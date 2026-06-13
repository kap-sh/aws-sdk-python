"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleDmarcOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOT_EQUALS",
    )
)


def serialize_aws_json_1_0(value: RuleDmarcOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleDmarcOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleDmarcOperator value: {data!r}")
    return cast(RuleDmarcOperator, data)

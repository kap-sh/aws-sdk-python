"""Generated from Smithy shape ``com.amazonaws.fms#RuleOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

RuleOrder: TypeAlias = Literal[
    "STRICT_ORDER",
    "DEFAULT_ACTION_ORDER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRICT_ORDER",
        "DEFAULT_ACTION_ORDER",
    )
)


def serialize_aws_json_1_1(value: RuleOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleOrder value: {data!r}")
    return cast(RuleOrder, data)

"""Generated from Smithy shape ``com.amazonaws.route53domains#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

Operator: TypeAlias = Literal[
    "LE",
    "GE",
    "BEGINS_WITH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LE",
        "GE",
        "BEGINS_WITH",
    )
)


def serialize_aws_json_1_1(value: Operator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)

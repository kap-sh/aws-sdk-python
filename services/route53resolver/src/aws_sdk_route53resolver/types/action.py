"""Generated from Smithy shape ``com.amazonaws.route53resolver#Action``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

Action: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
    "ALERT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "BLOCK",
        "ALERT",
    )
)


def serialize_aws_json_1_1(value: Action) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)

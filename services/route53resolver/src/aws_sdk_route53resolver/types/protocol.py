"""Generated from Smithy shape ``com.amazonaws.route53resolver#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "DoH",
    "Do53",
    "DoH-FIPS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DoH",
        "Do53",
        "DoH-FIPS",
    )
)


def serialize_aws_json_1_1(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)

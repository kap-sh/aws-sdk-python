"""Generated from Smithy shape ``com.amazonaws.route53resolver#ConfidenceThreshold``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

ConfidenceThreshold: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_aws_json_1_1(value: ConfidenceThreshold) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfidenceThreshold:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfidenceThreshold value: {data!r}")
    return cast(ConfidenceThreshold, data)

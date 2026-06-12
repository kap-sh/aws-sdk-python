"""Generated from Smithy shape ``com.amazonaws.b2bi#X12Version``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

X12Version: TypeAlias = Literal[
    "VERSION_4010",
    "VERSION_4030",
    "VERSION_4050",
    "VERSION_4060",
    "VERSION_5010",
    "VERSION_5010_HIPAA",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERSION_4010",
        "VERSION_4030",
        "VERSION_4050",
        "VERSION_4060",
        "VERSION_5010",
        "VERSION_5010_HIPAA",
    )
)


def serialize_aws_json_1_0(value: X12Version) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12Version:
    if data not in _VALUES:
        raise DeserializationError(f"unknown X12Version value: {data!r}")
    return cast(X12Version, data)

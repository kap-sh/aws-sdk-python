"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdict``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

RuleVerdict: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "GRAY",
    "PROCESSING_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "FAIL",
        "GRAY",
        "PROCESSING_FAILED",
    )
)


def serialize_aws_json_1_0(value: RuleVerdict) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleVerdict:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleVerdict value: {data!r}")
    return cast(RuleVerdict, data)

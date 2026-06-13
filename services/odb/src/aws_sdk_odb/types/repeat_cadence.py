"""Generated from Smithy shape ``com.amazonaws.odb#RepeatCadence``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

RepeatCadence: TypeAlias = Literal[
    "ONE_TIME",
    "WEEKLY",
    "MONTHLY",
    "YEARLY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_TIME",
        "WEEKLY",
        "MONTHLY",
        "YEARLY",
    )
)


def serialize_aws_json_1_0(value: RepeatCadence) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RepeatCadence:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepeatCadence value: {data!r}")
    return cast(RepeatCadence, data)

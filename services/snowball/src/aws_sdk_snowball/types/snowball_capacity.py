"""Generated from Smithy shape ``com.amazonaws.snowball#SnowballCapacity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

SnowballCapacity: TypeAlias = Literal[
    "T50",
    "T80",
    "T100",
    "T42",
    "T98",
    "T8",
    "T14",
    "T32",
    "NoPreference",
    "T240",
    "T13",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "T50",
        "T80",
        "T100",
        "T42",
        "T98",
        "T8",
        "T14",
        "T32",
        "NoPreference",
        "T240",
        "T13",
    )
)


def serialize_aws_json_1_1(value: SnowballCapacity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowballCapacity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnowballCapacity value: {data!r}")
    return cast(SnowballCapacity, data)

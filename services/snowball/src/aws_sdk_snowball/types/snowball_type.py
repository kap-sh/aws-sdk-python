"""Generated from Smithy shape ``com.amazonaws.snowball#SnowballType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

SnowballType: TypeAlias = Literal[
    "STANDARD",
    "EDGE",
    "EDGE_C",
    "EDGE_CG",
    "EDGE_S",
    "SNC1_HDD",
    "SNC1_SSD",
    "V3_5C",
    "V3_5S",
    "RACK_5U_C",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "EDGE",
        "EDGE_C",
        "EDGE_CG",
        "EDGE_S",
        "SNC1_HDD",
        "SNC1_SSD",
        "V3_5C",
        "V3_5S",
        "RACK_5U_C",
    )
)


def serialize_aws_json_1_1(value: SnowballType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowballType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnowballType value: {data!r}")
    return cast(SnowballType, data)

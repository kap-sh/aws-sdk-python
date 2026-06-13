"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AlarmType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

AlarmType: TypeAlias = Literal[
    "applicationHealth",
    "trigger",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "applicationHealth",
        "trigger",
    )
)


def serialize_aws_json_1_0(value: AlarmType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmType value: {data!r}")
    return cast(AlarmType, data)

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AlarmCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

AlarmCondition: TypeAlias = Literal[
    "red",
    "green",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "red",
        "green",
    )
)


def serialize_aws_json_1_0(value: AlarmCondition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmCondition value: {data!r}")
    return cast(AlarmCondition, data)

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RecoveryApproach``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

RecoveryApproach: TypeAlias = Literal[
    "activeActive",
    "activePassive",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "activeActive",
        "activePassive",
    )
)


def serialize_aws_json_1_0(value: RecoveryApproach) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecoveryApproach:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecoveryApproach value: {data!r}")
    return cast(RecoveryApproach, data)

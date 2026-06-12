"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationOutputTimingSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Global Configuration Output Timing Source"""
GlobalConfigurationOutputTimingSource: TypeAlias = Literal[
    "INPUT_CLOCK",
    "SYSTEM_CLOCK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPUT_CLOCK",
        "SYSTEM_CLOCK",
    )
)


def serialize_json(value: GlobalConfigurationOutputTimingSource) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationOutputTimingSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalConfigurationOutputTimingSource value: {data!r}"
        )
    return cast(GlobalConfigurationOutputTimingSource, data)

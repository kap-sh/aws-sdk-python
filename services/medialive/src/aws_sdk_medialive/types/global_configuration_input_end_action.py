"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationInputEndAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Global Configuration Input End Action"""
GlobalConfigurationInputEndAction: TypeAlias = Literal[
    "NONE",
    "SWITCH_AND_LOOP_INPUTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SWITCH_AND_LOOP_INPUTS",
    )
)


def serialize_json(value: GlobalConfigurationInputEndAction) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationInputEndAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalConfigurationInputEndAction value: {data!r}"
        )
    return cast(GlobalConfigurationInputEndAction, data)

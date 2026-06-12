"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationLowFramerateInputs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Global Configuration Low Framerate Inputs"""
GlobalConfigurationLowFramerateInputs: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: GlobalConfigurationLowFramerateInputs) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationLowFramerateInputs:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalConfigurationLowFramerateInputs value: {data!r}"
        )
    return cast(GlobalConfigurationLowFramerateInputs, data)

"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ObfuscationSetting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

ObfuscationSetting: TypeAlias = Literal[
    "NONE",
    "DEFAULT_OBFUSCATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DEFAULT_OBFUSCATION",
    )
)


def serialize_json(value: ObfuscationSetting) -> str:
    return value


def deserialize_json(data: str) -> ObfuscationSetting:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObfuscationSetting value: {data!r}")
    return cast(ObfuscationSetting, data)

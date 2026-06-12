"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ObfuscationSettingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ObfuscationSettingType: TypeAlias = Literal[
    "None",
    "DefaultObfuscation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "DefaultObfuscation",
    )
)


def serialize_json(value: ObfuscationSettingType) -> str:
    return value


def deserialize_json(data: str) -> ObfuscationSettingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObfuscationSettingType value: {data!r}")
    return cast(ObfuscationSettingType, data)

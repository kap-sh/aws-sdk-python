"""Generated from Smithy shape ``com.amazonaws.amplifybackend#MfaTypesElement``."""

from typing import Literal, TypeAlias, cast

MfaTypesElement: TypeAlias = Literal[
    "SMS",
    "TOTP",
]


# --- restJson1 ser/de ---
def serialize_json(value: MfaTypesElement) -> str:
    return value


def deserialize_json(data: str) -> MfaTypesElement:
    return cast(MfaTypesElement, data)

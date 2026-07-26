"""Generated from Smithy shape ``com.amazonaws.taxsettings#RegistrationType``."""

from typing import Literal, TypeAlias, cast

RegistrationType: TypeAlias = Literal[
    "Intra-EU",
    "Local",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationType) -> str:
    return value


def deserialize_json(data: str) -> RegistrationType:
    return cast(RegistrationType, data)

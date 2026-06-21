"""Generated from Smithy shape ``com.amazonaws.emrcontainers#PersistentAppUI``."""

from typing import Literal, TypeAlias, cast

PersistentAppUI: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PersistentAppUI) -> str:
    return value


def deserialize_json(data: str) -> PersistentAppUI:
    return cast(PersistentAppUI, data)

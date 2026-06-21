"""Generated from Smithy shape ``com.amazonaws.iot#ConfigName``."""

from typing import Literal, TypeAlias, cast

ConfigName: TypeAlias = Literal[
    "CERT_AGE_THRESHOLD_IN_DAYS",
    "CERT_EXPIRATION_THRESHOLD_IN_DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigName) -> str:
    return value


def deserialize_json(data: str) -> ConfigName:
    return cast(ConfigName, data)

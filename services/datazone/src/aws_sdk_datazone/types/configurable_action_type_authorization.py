"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableActionTypeAuthorization``."""

from typing import Literal, TypeAlias, cast

ConfigurableActionTypeAuthorization: TypeAlias = Literal[
    "IAM",
    "HTTPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableActionTypeAuthorization) -> str:
    return value


def deserialize_json(data: str) -> ConfigurableActionTypeAuthorization:
    return cast(ConfigurableActionTypeAuthorization, data)

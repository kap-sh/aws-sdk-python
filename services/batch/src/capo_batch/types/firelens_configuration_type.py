"""Generated from Smithy shape ``com.amazonaws.batch#FirelensConfigurationType``."""

from typing import Literal, TypeAlias, cast

FirelensConfigurationType: TypeAlias = Literal[
    "fluentd",
    "fluentbit",
]


# --- restJson1 ser/de ---
def serialize_json(value: FirelensConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> FirelensConfigurationType:
    return cast(FirelensConfigurationType, data)

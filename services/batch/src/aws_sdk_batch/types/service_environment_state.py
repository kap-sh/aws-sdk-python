"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentState``."""

from typing import Literal, TypeAlias, cast

ServiceEnvironmentState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentState) -> str:
    return value


def deserialize_json(data: str) -> ServiceEnvironmentState:
    return cast(ServiceEnvironmentState, data)

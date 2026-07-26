"""Generated from Smithy shape ``com.amazonaws.appconfig#EnvironmentState``."""

from typing import Literal, TypeAlias, cast

EnvironmentState: TypeAlias = Literal[
    "READY_FOR_DEPLOYMENT",
    "DEPLOYING",
    "ROLLING_BACK",
    "ROLLED_BACK",
    "REVERTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentState) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentState:
    return cast(EnvironmentState, data)

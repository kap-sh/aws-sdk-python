"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchedulingConfigEndBehavior``."""

from typing import Literal, TypeAlias, cast

SchedulingConfigEndBehavior: TypeAlias = Literal[
    "STOP_ROLLOUT",
    "CANCEL",
    "FORCE_CANCEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingConfigEndBehavior) -> str:
    return value


def deserialize_json(data: str) -> SchedulingConfigEndBehavior:
    return cast(SchedulingConfigEndBehavior, data)

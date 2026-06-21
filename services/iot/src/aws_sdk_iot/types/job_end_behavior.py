"""Generated from Smithy shape ``com.amazonaws.iot#JobEndBehavior``."""

from typing import Literal, TypeAlias, cast

JobEndBehavior: TypeAlias = Literal[
    "STOP_ROLLOUT",
    "CANCEL",
    "FORCE_CANCEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobEndBehavior) -> str:
    return value


def deserialize_json(data: str) -> JobEndBehavior:
    return cast(JobEndBehavior, data)

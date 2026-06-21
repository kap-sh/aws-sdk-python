"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#StatusType``."""

from typing import Literal, TypeAlias, cast

StatusType: TypeAlias = Literal[
    "Deployment",
    "AsyncExecutions",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusType) -> str:
    return value


def deserialize_json(data: str) -> StatusType:
    return cast(StatusType, data)

"""Generated from Smithy shape ``com.amazonaws.deadline#DesiredWorkerStatus``."""

from typing import Literal, TypeAlias, cast

DesiredWorkerStatus: TypeAlias = Literal["STOPPED",]


# --- restJson1 ser/de ---
def serialize_json(value: DesiredWorkerStatus) -> str:
    return value


def deserialize_json(data: str) -> DesiredWorkerStatus:
    return cast(DesiredWorkerStatus, data)

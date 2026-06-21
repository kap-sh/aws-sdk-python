"""Generated from Smithy shape ``com.amazonaws.appfabric#ResultStatus``."""

from typing import Literal, TypeAlias, cast

ResultStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResultStatus) -> str:
    return value


def deserialize_json(data: str) -> ResultStatus:
    return cast(ResultStatus, data)

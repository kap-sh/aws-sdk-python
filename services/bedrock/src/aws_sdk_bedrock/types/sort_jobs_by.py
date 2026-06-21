"""Generated from Smithy shape ``com.amazonaws.bedrock#SortJobsBy``."""

from typing import Literal, TypeAlias, cast

SortJobsBy: TypeAlias = Literal["CreationTime",]


# --- restJson1 ser/de ---
def serialize_json(value: SortJobsBy) -> str:
    return value


def deserialize_json(data: str) -> SortJobsBy:
    return cast(SortJobsBy, data)

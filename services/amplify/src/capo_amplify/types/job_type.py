"""Generated from Smithy shape ``com.amazonaws.amplify#JobType``."""

from typing import Literal, TypeAlias, cast

JobType: TypeAlias = Literal[
    "RELEASE",
    "RETRY",
    "MANUAL",
    "WEB_HOOK",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    return cast(JobType, data)

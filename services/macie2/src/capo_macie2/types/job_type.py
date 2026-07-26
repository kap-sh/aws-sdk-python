"""Generated from Smithy shape ``com.amazonaws.macie2#JobType``."""

from typing import Literal, TypeAlias, cast

"""<p>The schedule for running a classification job. Valid values are:</p>"""
JobType: TypeAlias = Literal[
    "ONE_TIME",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    return cast(JobType, data)

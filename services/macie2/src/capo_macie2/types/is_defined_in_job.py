"""Generated from Smithy shape ``com.amazonaws.macie2#IsDefinedInJob``."""

from typing import Literal, TypeAlias, cast

IsDefinedInJob: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsDefinedInJob) -> str:
    return value


def deserialize_json(data: str) -> IsDefinedInJob:
    return cast(IsDefinedInJob, data)

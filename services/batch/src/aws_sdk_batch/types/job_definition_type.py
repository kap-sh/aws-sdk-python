"""Generated from Smithy shape ``com.amazonaws.batch#JobDefinitionType``."""

from typing import Literal, TypeAlias, cast

JobDefinitionType: TypeAlias = Literal[
    "container",
    "multinode",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobDefinitionType) -> str:
    return value


def deserialize_json(data: str) -> JobDefinitionType:
    return cast(JobDefinitionType, data)

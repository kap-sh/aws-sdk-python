"""Generated from Smithy shape ``com.amazonaws.medialive#PipelineId``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Pipeline ID"""
PipelineId: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PIPELINE_0",
        "PIPELINE_1",
    )
)


def serialize_json(value: PipelineId) -> str:
    return value


def deserialize_json(data: str) -> PipelineId:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineId value: {data!r}")
    return cast(PipelineId, data)

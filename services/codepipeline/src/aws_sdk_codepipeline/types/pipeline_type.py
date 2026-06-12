"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

PipelineType: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1",
        "V2",
    )
)


def serialize_aws_json_1_1(value: PipelineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineType value: {data!r}")
    return cast(PipelineType, data)

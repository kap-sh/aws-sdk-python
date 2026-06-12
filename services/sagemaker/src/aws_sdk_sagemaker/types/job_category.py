"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

JobCategory: TypeAlias = Literal[
    "AgentRFT",
    "AgentRFTEvaluation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AgentRFT",
        "AgentRFTEvaluation",
    )
)


def serialize_aws_json_1_1(value: JobCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobCategory value: {data!r}")
    return cast(JobCategory, data)

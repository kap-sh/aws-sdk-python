"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#JobFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

JobFilterName: TypeAlias = Literal[
    "ResourceType",
    "JobStatus",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceType",
        "JobStatus",
    )
)


def serialize_aws_json_1_0(value: JobFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> JobFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobFilterName value: {data!r}")
    return cast(JobFilterName, data)

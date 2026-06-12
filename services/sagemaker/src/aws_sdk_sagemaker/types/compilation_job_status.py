"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompilationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CompilationJobStatus: TypeAlias = Literal[
    "INPROGRESS",
    "COMPLETED",
    "FAILED",
    "STARTING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPROGRESS",
        "COMPLETED",
        "FAILED",
        "STARTING",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: CompilationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompilationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompilationJobStatus value: {data!r}")
    return cast(CompilationJobStatus, data)

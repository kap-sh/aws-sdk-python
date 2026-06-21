"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompilationJobStatus``."""

from typing import Literal, TypeAlias, cast

CompilationJobStatus: TypeAlias = Literal[
    "INPROGRESS",
    "COMPLETED",
    "FAILED",
    "STARTING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompilationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompilationJobStatus:
    return cast(CompilationJobStatus, data)

"""Generated from Smithy shape ``com.amazonaws.emr#ExecutionEngineType``."""

from typing import Literal, TypeAlias, cast

ExecutionEngineType: TypeAlias = Literal["EMR",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionEngineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionEngineType:
    return cast(ExecutionEngineType, data)

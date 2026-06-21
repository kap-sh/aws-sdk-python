"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionFilterKey``."""

from typing import Literal, TypeAlias, cast

AssociationExecutionFilterKey: TypeAlias = Literal[
    "ExecutionId",
    "Status",
    "CreatedTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationExecutionFilterKey:
    return cast(AssociationExecutionFilterKey, data)

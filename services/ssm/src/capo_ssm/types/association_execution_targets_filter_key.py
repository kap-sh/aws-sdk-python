"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTargetsFilterKey``."""

from typing import Literal, TypeAlias, cast

AssociationExecutionTargetsFilterKey: TypeAlias = Literal[
    "Status",
    "ResourceId",
    "ResourceType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionTargetsFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationExecutionTargetsFilterKey:
    return cast(AssociationExecutionTargetsFilterKey, data)

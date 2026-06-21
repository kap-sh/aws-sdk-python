"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

FlowDefinitionStatus: TypeAlias = Literal[
    "Initializing",
    "Active",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowDefinitionStatus:
    return cast(FlowDefinitionStatus, data)

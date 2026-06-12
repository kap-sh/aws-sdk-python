"""Generated from Smithy shape ``com.amazonaws.sagemaker#Edges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge

Edges: TypeAlias = list["aws_sdk_sagemaker.types.edge.Edge"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Edges) -> list:
    import aws_sdk_sagemaker.types.edge

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.edge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Edges:
    import aws_sdk_sagemaker.types.edge

    out: Edges = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.edge.deserialize_aws_json_1_1(item))
    return out

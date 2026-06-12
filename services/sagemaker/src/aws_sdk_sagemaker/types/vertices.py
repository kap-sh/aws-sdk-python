"""Generated from Smithy shape ``com.amazonaws.sagemaker#Vertices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.vertex

Vertices: TypeAlias = list["aws_sdk_sagemaker.types.vertex.Vertex"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Vertices) -> list:
    import aws_sdk_sagemaker.types.vertex

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.vertex.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Vertices:
    import aws_sdk_sagemaker.types.vertex

    out: Vertices = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.vertex.deserialize_aws_json_1_1(item))
    return out

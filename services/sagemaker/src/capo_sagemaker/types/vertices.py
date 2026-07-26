"""Generated from Smithy shape ``com.amazonaws.sagemaker#Vertices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.vertex

Vertices: TypeAlias = list["capo_sagemaker.types.vertex.Vertex"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Vertices) -> list:
    import capo_sagemaker.types.vertex

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.vertex.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Vertices:
    import capo_sagemaker.types.vertex

    out: Vertices = []
    for item in data:
        out.append(capo_sagemaker.types.vertex.deserialize_aws_json_1_1(item))
    return out

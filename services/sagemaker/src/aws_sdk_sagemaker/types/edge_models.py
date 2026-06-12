"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_model

EdgeModels: TypeAlias = list["aws_sdk_sagemaker.types.edge_model.EdgeModel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeModels) -> list:
    import aws_sdk_sagemaker.types.edge_model

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.edge_model.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeModels:
    import aws_sdk_sagemaker.types.edge_model

    out: EdgeModels = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.edge_model.deserialize_aws_json_1_1(item))
    return out

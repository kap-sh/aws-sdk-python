"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeModelStats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_model_stat

EdgeModelStats: TypeAlias = list[
    "aws_sdk_sagemaker.types.edge_model_stat.EdgeModelStat"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeModelStats) -> list:
    import aws_sdk_sagemaker.types.edge_model_stat

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.edge_model_stat.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EdgeModelStats:
    import aws_sdk_sagemaker.types.edge_model_stat

    out: EdgeModelStats = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.edge_model_stat.deserialize_aws_json_1_1(item)
        )
    return out

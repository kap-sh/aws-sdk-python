"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActiveOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.active_cluster_operation_count
    import aws_sdk_sagemaker.types.active_cluster_operation_name

ActiveOperations: TypeAlias = dict[
    "aws_sdk_sagemaker.types.active_cluster_operation_name.ActiveClusterOperationName",
    "aws_sdk_sagemaker.types.active_cluster_operation_count.ActiveClusterOperationCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ActiveOperations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sagemaker.types.active_cluster_operation_name

        out[
            aws_sdk_sagemaker.types.active_cluster_operation_name.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveOperations:
    out: ActiveOperations = {}
    for key, value in data.items():
        import aws_sdk_sagemaker.types.active_cluster_operation_name

        out[
            aws_sdk_sagemaker.types.active_cluster_operation_name.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out

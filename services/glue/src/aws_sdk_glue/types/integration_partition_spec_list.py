"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationPartitionSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_partition

IntegrationPartitionSpecList: TypeAlias = list[
    "aws_sdk_glue.types.integration_partition.IntegrationPartition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationPartitionSpecList) -> list:
    import aws_sdk_glue.types.integration_partition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.integration_partition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegrationPartitionSpecList:
    import aws_sdk_glue.types.integration_partition

    out: IntegrationPartitionSpecList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.integration_partition.deserialize_aws_json_1_1(item)
        )
    return out

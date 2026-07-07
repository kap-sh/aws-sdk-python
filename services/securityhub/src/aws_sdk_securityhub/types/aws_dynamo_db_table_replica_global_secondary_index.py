"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableReplicaGlobalSecondaryIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override
    import aws_sdk_securityhub.types.non_empty_string


class AwsDynamoDbTableReplicaGlobalSecondaryIndex(TypedDict, closed=True):
    index_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the index.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override.AwsDynamoDbTableProvisionedThroughputOverride"
    ]
    """<p>Replica-specific configuration for the provisioned throughput for the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableReplicaGlobalSecondaryIndex) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "provisioned_throughput_override" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override

        out["ProvisionedThroughputOverride"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override.serialize_json(
                value["provisioned_throughput_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableReplicaGlobalSecondaryIndex:
    out: AwsDynamoDbTableReplicaGlobalSecondaryIndex = {}  # type: ignore[typeddict-item]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "ProvisionedThroughputOverride" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override

        out["provisioned_throughput_override"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override.deserialize_json(
                data["ProvisionedThroughputOverride"]
            )
        )
    return out

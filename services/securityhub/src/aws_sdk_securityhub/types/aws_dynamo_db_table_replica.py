"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableReplica``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override
    import aws_sdk_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsDynamoDbTableReplica(TypedDict):
    global_secondary_indexes: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index_list.AwsDynamoDbTableReplicaGlobalSecondaryIndexList"
    ]
    """<p>List of global secondary indexes for the replica.</p>"""
    kms_master_key_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the KMS key that will be used for KMS encryption for the replica.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override.AwsDynamoDbTableProvisionedThroughputOverride"
    ]
    """<p>Replica-specific configuration for the provisioned throughput.</p>"""
    region_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the Region where the replica is located.</p>"""
    replica_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current status of the replica. Valid values are as follows:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATING</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>DELETING</code> </p> </li> <li> <p> <code>UPDATING</code> </p> </li> </ul>"""
    replica_status_description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Detailed information about the replica status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableReplica) -> dict:
    out: dict = {}
    if "global_secondary_indexes" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index_list.serialize_json(
                value["global_secondary_indexes"]
            )
        )
    if "kms_master_key_id" in value:
        out["KmsMasterKeyId"] = value["kms_master_key_id"]
    if "provisioned_throughput_override" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override

        out["ProvisionedThroughputOverride"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override.serialize_json(
                value["provisioned_throughput_override"]
            )
        )
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    if "replica_status" in value:
        out["ReplicaStatus"] = value["replica_status"]
    if "replica_status_description" in value:
        out["ReplicaStatusDescription"] = value["replica_status_description"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableReplica:
    out: AwsDynamoDbTableReplica = {}  # type: ignore[typeddict-item]
    if "GlobalSecondaryIndexes" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index_list

        out["global_secondary_indexes"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index_list.deserialize_json(
                data["GlobalSecondaryIndexes"]
            )
        )
    if "KmsMasterKeyId" in data:
        out["kms_master_key_id"] = data["KmsMasterKeyId"]
    if "ProvisionedThroughputOverride" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override

        out["provisioned_throughput_override"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput_override.deserialize_json(
                data["ProvisionedThroughputOverride"]
            )
        )
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    if "ReplicaStatus" in data:
        out["replica_status"] = data["ReplicaStatus"]
    if "ReplicaStatusDescription" in data:
        out["replica_status_description"] = data["ReplicaStatusDescription"]
    return out

"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateReplicationGroupMemberAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kms_master_key_id
    import aws_sdk_dynamodb.types.on_demand_throughput_override
    import aws_sdk_dynamodb.types.provisioned_throughput_override
    import aws_sdk_dynamodb.types.region_name
    import aws_sdk_dynamodb.types.replica_global_secondary_index_list
    import aws_sdk_dynamodb.types.table_class


class UpdateReplicationGroupMemberAction(TypedDict, closed=True):
    region_name: "aws_sdk_dynamodb.types.region_name.RegionName"
    """<p>The Region where the replica exists.</p>"""
    kms_master_key_id: NotRequired[
        "aws_sdk_dynamodb.types.kms_master_key_id.KMSMasterKeyId"
    ]
    """<p>The KMS key of the replica that should be used for KMS encryption. To specify a key, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS key <code>alias/aws/dynamodb</code>.</p>"""
    provisioned_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.provisioned_throughput_override.ProvisionedThroughputOverride"
    ]
    """<p>Replica-specific provisioned throughput. If not specified, uses the source table's provisioned throughput settings.</p>"""
    on_demand_throughput_override: NotRequired[
        "aws_sdk_dynamodb.types.on_demand_throughput_override.OnDemandThroughputOverride"
    ]
    """<p>Overrides the maximum on-demand throughput for the replica table.</p>"""
    global_secondary_indexes: NotRequired[
        "aws_sdk_dynamodb.types.replica_global_secondary_index_list.ReplicaGlobalSecondaryIndexList"
    ]
    """<p>Replica-specific global secondary index settings.</p>"""
    table_class_override: NotRequired["aws_sdk_dynamodb.types.table_class.TableClass"]
    """<p>Replica-specific table class. If not specified, uses the source table's table class.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateReplicationGroupMemberAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    if "kms_master_key_id" in value:
        out["KMSMasterKeyId"] = value["kms_master_key_id"]
    if "provisioned_throughput_override" in value:
        import aws_sdk_dynamodb.types.provisioned_throughput_override

        out["ProvisionedThroughputOverride"] = (
            aws_sdk_dynamodb.types.provisioned_throughput_override.serialize_aws_json_1_0(
                value["provisioned_throughput_override"]
            )
        )
    if "on_demand_throughput_override" in value:
        import aws_sdk_dynamodb.types.on_demand_throughput_override

        out["OnDemandThroughputOverride"] = (
            aws_sdk_dynamodb.types.on_demand_throughput_override.serialize_aws_json_1_0(
                value["on_demand_throughput_override"]
            )
        )
    if "global_secondary_indexes" in value:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_list

        out["GlobalSecondaryIndexes"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_list.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    if "table_class_override" in value:
        import aws_sdk_dynamodb.types.table_class

        out["TableClassOverride"] = (
            aws_sdk_dynamodb.types.table_class.serialize_aws_json_1_0(
                value["table_class_override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateReplicationGroupMemberAction:
    out: UpdateReplicationGroupMemberAction = {}  # type: ignore[typeddict-item]
    if "RegionName" in data:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError(
            "UpdateReplicationGroupMemberAction.region_name required"
        )
    if "KMSMasterKeyId" in data:
        out["kms_master_key_id"] = data["KMSMasterKeyId"]
    if "ProvisionedThroughputOverride" in data:
        import aws_sdk_dynamodb.types.provisioned_throughput_override

        out["provisioned_throughput_override"] = (
            aws_sdk_dynamodb.types.provisioned_throughput_override.deserialize_aws_json_1_0(
                data["ProvisionedThroughputOverride"]
            )
        )
    if "OnDemandThroughputOverride" in data:
        import aws_sdk_dynamodb.types.on_demand_throughput_override

        out["on_demand_throughput_override"] = (
            aws_sdk_dynamodb.types.on_demand_throughput_override.deserialize_aws_json_1_0(
                data["OnDemandThroughputOverride"]
            )
        )
    if "GlobalSecondaryIndexes" in data:
        import aws_sdk_dynamodb.types.replica_global_secondary_index_list

        out["global_secondary_indexes"] = (
            aws_sdk_dynamodb.types.replica_global_secondary_index_list.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    if "TableClassOverride" in data:
        import aws_sdk_dynamodb.types.table_class

        out["table_class_override"] = (
            aws_sdk_dynamodb.types.table_class.deserialize_aws_json_1_0(
                data["TableClassOverride"]
            )
        )
    return out

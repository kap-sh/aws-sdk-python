"""Generated from Smithy shape ``com.amazonaws.docdbelastic#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.auth
    import aws_sdk_docdb_elastic.types.shard_list
    import aws_sdk_docdb_elastic.types.status
    import aws_sdk_docdb_elastic.types.string_list


class Cluster(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The name of the elastic cluster.</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    status: "aws_sdk_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster.</p>"""
    cluster_endpoint: "str"
    """<p>The URL used to connect to the elastic cluster.</p>"""
    create_time: "str"
    """<p>The time when the elastic cluster was created in Universal Coordinated Time (UTC).</p>"""
    admin_user_name: "str"
    """<p>The name of the elastic cluster administrator.</p>"""
    auth_type: "aws_sdk_docdb_elastic.types.auth.Auth"
    """<p>The authentication type for the elastic cluster.</p>"""
    shard_capacity: "int"
    """<p>The number of vCPUs assigned to each elastic cluster shard. Maximum is 64. Allowed values are 2, 4, 8, 16, 32, 64.</p>"""
    shard_count: "int"
    """<p>The number of shards assigned to the elastic cluster. Maximum is 32.</p>"""
    vpc_security_group_ids: "aws_sdk_docdb_elastic.types.string_list.StringList"
    """<p>A list of EC2 VPC security groups associated with thie elastic cluster.</p>"""
    subnet_ids: "aws_sdk_docdb_elastic.types.string_list.StringList"
    """<p>The Amazon EC2 subnet IDs for the elastic cluster.</p>"""
    preferred_maintenance_window: "str"
    """<p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> <i>Format</i>: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p>"""
    kms_key_id: "str"
    """<p>The KMS key identifier to use to encrypt the elastic cluster.</p>"""
    shards: NotRequired["aws_sdk_docdb_elastic.types.shard_list.ShardList"]
    """<p>The total number of shards in the cluster.</p>"""
    backup_retention_period: NotRequired["int"]
    """<p>The number of days for which automatic snapshots are retained.</p>"""
    preferred_backup_window: NotRequired["str"]
    """<p>The daily time range during which automated backups are created if automated backups are enabled, as determined by <code>backupRetentionPeriod</code>.</p>"""
    shard_instance_count: NotRequired["int"]
    """<p>The number of replica instances applying to all shards in the cluster. A <code>shardInstanceCount</code> value of 1 means there is one writer instance, and any additional instances are replicas that can be used for reads and to improve availability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cluster) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    out["clusterArn"] = value["cluster_arn"]
    out["status"] = value["status"]
    out["clusterEndpoint"] = value["cluster_endpoint"]
    out["createTime"] = value["create_time"]
    out["adminUserName"] = value["admin_user_name"]
    out["authType"] = value["auth_type"]
    out["shardCapacity"] = value["shard_capacity"]
    out["shardCount"] = value["shard_count"]
    import aws_sdk_docdb_elastic.types.string_list

    out["vpcSecurityGroupIds"] = aws_sdk_docdb_elastic.types.string_list.serialize_json(
        value["vpc_security_group_ids"]
    )
    import aws_sdk_docdb_elastic.types.string_list

    out["subnetIds"] = aws_sdk_docdb_elastic.types.string_list.serialize_json(
        value["subnet_ids"]
    )
    out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "shards" in value:
        import aws_sdk_docdb_elastic.types.shard_list

        out["shards"] = aws_sdk_docdb_elastic.types.shard_list.serialize_json(
            value["shards"]
        )
    if "backup_retention_period" in value:
        out["backupRetentionPeriod"] = value["backup_retention_period"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "shard_instance_count" in value:
        out["shardInstanceCount"] = value["shard_instance_count"]
    return out


def deserialize_json(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("Cluster.cluster_name required")
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("Cluster.cluster_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("Cluster.status required")
    if "clusterEndpoint" in data:
        out["cluster_endpoint"] = data["clusterEndpoint"]
    else:
        raise DeserializationError("Cluster.cluster_endpoint required")
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    else:
        raise DeserializationError("Cluster.create_time required")
    if "adminUserName" in data:
        out["admin_user_name"] = data["adminUserName"]
    else:
        raise DeserializationError("Cluster.admin_user_name required")
    if "authType" in data:
        out["auth_type"] = data["authType"]
    else:
        raise DeserializationError("Cluster.auth_type required")
    if "shardCapacity" in data:
        out["shard_capacity"] = data["shardCapacity"]
    else:
        raise DeserializationError("Cluster.shard_capacity required")
    if "shardCount" in data:
        out["shard_count"] = data["shardCount"]
    else:
        raise DeserializationError("Cluster.shard_count required")
    if "vpcSecurityGroupIds" in data:
        import aws_sdk_docdb_elastic.types.string_list

        out["vpc_security_group_ids"] = (
            aws_sdk_docdb_elastic.types.string_list.deserialize_json(
                data["vpcSecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("Cluster.vpc_security_group_ids required")
    if "subnetIds" in data:
        import aws_sdk_docdb_elastic.types.string_list

        out["subnet_ids"] = aws_sdk_docdb_elastic.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("Cluster.subnet_ids required")
    if "preferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    else:
        raise DeserializationError("Cluster.preferred_maintenance_window required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("Cluster.kms_key_id required")
    if "shards" in data:
        import aws_sdk_docdb_elastic.types.shard_list

        out["shards"] = aws_sdk_docdb_elastic.types.shard_list.deserialize_json(
            data["shards"]
        )
    if "backupRetentionPeriod" in data:
        out["backup_retention_period"] = data["backupRetentionPeriod"]
    if "preferredBackupWindow" in data:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if "shardInstanceCount" in data:
        out["shard_instance_count"] = data["shardInstanceCount"]
    return out

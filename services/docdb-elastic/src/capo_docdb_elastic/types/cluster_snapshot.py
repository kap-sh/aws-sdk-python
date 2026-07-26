"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import capo_docdb_elastic.types.snapshot_type
    import capo_docdb_elastic.types.status
    import capo_docdb_elastic.types.string_list


class ClusterSnapshot(TypedDict, closed=True):
    subnet_ids: "capo_docdb_elastic.types.string_list.StringList"
    """<p>The Amazon EC2 subnet IDs for the elastic cluster.</p>"""
    snapshot_name: "str"
    """<p>The name of the elastic cluster snapshot.</p>"""
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot.</p>"""
    snapshot_creation_time: "str"
    """<p>The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).</p>"""
    cluster_arn: "str"
    """<p>The ARN identifier of the elastic cluster.</p>"""
    cluster_creation_time: "str"
    """<p>The time when the elastic cluster was created in Universal Coordinated Time (UTC).</p>"""
    status: "capo_docdb_elastic.types.status.Status"
    """<p>The status of the elastic cluster snapshot.</p>"""
    vpc_security_group_ids: "capo_docdb_elastic.types.string_list.StringList"
    """<p>A list of EC2 VPC security groups to associate with the elastic cluster.</p>"""
    admin_user_name: "str"
    """<p>The name of the elastic cluster administrator.</p>"""
    kms_key_id: "str"
    """<p>The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region. </p>"""
    snapshot_type: NotRequired["capo_docdb_elastic.types.snapshot_type.SnapshotType"]
    """<p>The type of cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> - Return all cluster snapshots that you have manually created for your Amazon Web Services account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterSnapshot) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.string_list

    out["subnetIds"] = capo_docdb_elastic.types.string_list.serialize_json(
        value["subnet_ids"]
    )
    out["snapshotName"] = value["snapshot_name"]
    out["snapshotArn"] = value["snapshot_arn"]
    out["snapshotCreationTime"] = value["snapshot_creation_time"]
    out["clusterArn"] = value["cluster_arn"]
    out["clusterCreationTime"] = value["cluster_creation_time"]
    out["status"] = value["status"]
    import capo_docdb_elastic.types.string_list

    out["vpcSecurityGroupIds"] = capo_docdb_elastic.types.string_list.serialize_json(
        value["vpc_security_group_ids"]
    )
    out["adminUserName"] = value["admin_user_name"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "snapshot_type" in value:
        out["snapshotType"] = value["snapshot_type"]
    return out


def deserialize_json(data: dict) -> ClusterSnapshot:
    out: ClusterSnapshot = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import capo_docdb_elastic.types.string_list

        out["subnet_ids"] = capo_docdb_elastic.types.string_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("ClusterSnapshot.subnet_ids required")
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError("ClusterSnapshot.snapshot_name required")
    if "snapshotArn" in data:
        out["snapshot_arn"] = data["snapshotArn"]
    else:
        raise DeserializationError("ClusterSnapshot.snapshot_arn required")
    if "snapshotCreationTime" in data:
        out["snapshot_creation_time"] = data["snapshotCreationTime"]
    else:
        raise DeserializationError("ClusterSnapshot.snapshot_creation_time required")
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("ClusterSnapshot.cluster_arn required")
    if "clusterCreationTime" in data:
        out["cluster_creation_time"] = data["clusterCreationTime"]
    else:
        raise DeserializationError("ClusterSnapshot.cluster_creation_time required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ClusterSnapshot.status required")
    if "vpcSecurityGroupIds" in data:
        import capo_docdb_elastic.types.string_list

        out["vpc_security_group_ids"] = (
            capo_docdb_elastic.types.string_list.deserialize_json(
                data["vpcSecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError("ClusterSnapshot.vpc_security_group_ids required")
    if "adminUserName" in data:
        out["admin_user_name"] = data["adminUserName"]
    else:
        raise DeserializationError("ClusterSnapshot.admin_user_name required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("ClusterSnapshot.kms_key_id required")
    if "snapshotType" in data:
        out["snapshot_type"] = data["snapshotType"]
    return out

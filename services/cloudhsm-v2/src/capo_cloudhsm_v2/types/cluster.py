"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup_id
    import capo_cloudhsm_v2.types.backup_policy
    import capo_cloudhsm_v2.types.backup_retention_policy
    import capo_cloudhsm_v2.types.certificates
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.cluster_mode
    import capo_cloudhsm_v2.types.cluster_state
    import capo_cloudhsm_v2.types.external_subnet_mapping
    import capo_cloudhsm_v2.types.hsm_type
    import capo_cloudhsm_v2.types.hsms
    import capo_cloudhsm_v2.types.network_type
    import capo_cloudhsm_v2.types.pre_co_password
    import capo_cloudhsm_v2.types.security_group
    import capo_cloudhsm_v2.types.state_message
    import capo_cloudhsm_v2.types.tag_list
    import capo_cloudhsm_v2.types.timestamp
    import capo_cloudhsm_v2.types.vpc_id


class Cluster(TypedDict, closed=True):
    backup_policy: NotRequired["capo_cloudhsm_v2.types.backup_policy.BackupPolicy"]
    """<p>The cluster's backup policy.</p>"""
    backup_retention_policy: NotRequired[
        "capo_cloudhsm_v2.types.backup_retention_policy.BackupRetentionPolicy"
    ]
    """<p>A policy that defines how the service retains backups.</p>"""
    cluster_id: NotRequired["capo_cloudhsm_v2.types.cluster_id.ClusterId"]
    """<p>The cluster's identifier (ID).</p>"""
    create_timestamp: NotRequired["capo_cloudhsm_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the cluster was created.</p>"""
    hsms: NotRequired["capo_cloudhsm_v2.types.hsms.Hsms"]
    """<p>Contains information about the HSMs in the cluster.</p>"""
    hsm_type: NotRequired["capo_cloudhsm_v2.types.hsm_type.HsmType"]
    """<p>The type of HSM that the cluster contains.</p>"""
    hsm_type_rollback_expiration: NotRequired[
        "capo_cloudhsm_v2.types.timestamp.Timestamp"
    ]
    """<p>The timestamp until when the cluster can be rolled back to its original HSM type.</p>"""
    pre_co_password: NotRequired["capo_cloudhsm_v2.types.pre_co_password.PreCoPassword"]
    """<p>The default password for the cluster's Pre-Crypto Officer (PRECO) user.</p>"""
    security_group: NotRequired["capo_cloudhsm_v2.types.security_group.SecurityGroup"]
    """<p>The identifier (ID) of the cluster's security group.</p>"""
    source_backup_id: NotRequired["capo_cloudhsm_v2.types.backup_id.BackupId"]
    """<p>The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.</p>"""
    state: NotRequired["capo_cloudhsm_v2.types.cluster_state.ClusterState"]
    """<p>The cluster's state.</p>"""
    state_message: NotRequired["capo_cloudhsm_v2.types.state_message.StateMessage"]
    """<p>A description of the cluster's state.</p>"""
    subnet_mapping: NotRequired[
        "capo_cloudhsm_v2.types.external_subnet_mapping.ExternalSubnetMapping"
    ]
    """<p>A map from availability zone to the cluster’s subnet in that availability zone.</p>"""
    vpc_id: NotRequired["capo_cloudhsm_v2.types.vpc_id.VpcId"]
    """<p>The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.</p>"""
    network_type: NotRequired["capo_cloudhsm_v2.types.network_type.NetworkType"]
    """<p>The cluster's NetworkType can be IPv4 (the default) or DUALSTACK. The IPv4 NetworkType restricts communication between your application and the hardware security modules (HSMs) to the IPv4 protocol only. The DUALSTACK NetworkType enables communication over both IPv4 and IPv6 protocols. To use DUALSTACK, configure your virtual private cloud (VPC) and subnets to support both IPv4 and IPv6. This configuration involves adding IPv6 Classless Inter-Domain Routing (CIDR) blocks to the existing IPv4 CIDR blocks in your subnets. The NetworkType you choose affects the network addressing options for your cluster. DUALSTACK provides more flexibility by supporting both IPv4 and IPv6 communication.</p>"""
    certificates: NotRequired["capo_cloudhsm_v2.types.certificates.Certificates"]
    """<p>Contains one or more certificates or a certificate signing request (CSR).</p>"""
    tag_list: NotRequired["capo_cloudhsm_v2.types.tag_list.TagList"]
    """<p>The list of tags for the cluster.</p>"""
    mode: NotRequired["capo_cloudhsm_v2.types.cluster_mode.ClusterMode"]
    """<p>The mode of the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cluster) -> dict:
    out: dict = {}
    if "backup_policy" in value:
        import capo_cloudhsm_v2.types.backup_policy

        out["BackupPolicy"] = (
            capo_cloudhsm_v2.types.backup_policy.serialize_aws_json_1_1(
                value["backup_policy"]
            )
        )
    if "backup_retention_policy" in value:
        import capo_cloudhsm_v2.types.backup_retention_policy

        out["BackupRetentionPolicy"] = (
            capo_cloudhsm_v2.types.backup_retention_policy.serialize_aws_json_1_1(
                value["backup_retention_policy"]
            )
        )
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "create_timestamp" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["CreateTimestamp"] = (
            capo_cloudhsm_v2.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "hsms" in value:
        import capo_cloudhsm_v2.types.hsms

        out["Hsms"] = capo_cloudhsm_v2.types.hsms.serialize_aws_json_1_1(value["hsms"])
    if "hsm_type" in value:
        out["HsmType"] = value["hsm_type"]
    if "hsm_type_rollback_expiration" in value:
        import capo_cloudhsm_v2.types.timestamp

        out["HsmTypeRollbackExpiration"] = (
            capo_cloudhsm_v2.types.timestamp.serialize_aws_json_1_1(
                value["hsm_type_rollback_expiration"]
            )
        )
    if "pre_co_password" in value:
        out["PreCoPassword"] = value["pre_co_password"]
    if "security_group" in value:
        out["SecurityGroup"] = value["security_group"]
    if "source_backup_id" in value:
        out["SourceBackupId"] = value["source_backup_id"]
    if "state" in value:
        import capo_cloudhsm_v2.types.cluster_state

        out["State"] = capo_cloudhsm_v2.types.cluster_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_message" in value:
        out["StateMessage"] = value["state_message"]
    if "subnet_mapping" in value:
        import capo_cloudhsm_v2.types.external_subnet_mapping

        out["SubnetMapping"] = (
            capo_cloudhsm_v2.types.external_subnet_mapping.serialize_aws_json_1_1(
                value["subnet_mapping"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "network_type" in value:
        import capo_cloudhsm_v2.types.network_type

        out["NetworkType"] = capo_cloudhsm_v2.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    if "certificates" in value:
        import capo_cloudhsm_v2.types.certificates

        out["Certificates"] = (
            capo_cloudhsm_v2.types.certificates.serialize_aws_json_1_1(
                value["certificates"]
            )
        )
    if "tag_list" in value:
        import capo_cloudhsm_v2.types.tag_list

        out["TagList"] = capo_cloudhsm_v2.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    if "mode" in value:
        import capo_cloudhsm_v2.types.cluster_mode

        out["Mode"] = capo_cloudhsm_v2.types.cluster_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "BackupPolicy" in data:
        import capo_cloudhsm_v2.types.backup_policy

        out["backup_policy"] = (
            capo_cloudhsm_v2.types.backup_policy.deserialize_aws_json_1_1(
                data["BackupPolicy"]
            )
        )
    if "BackupRetentionPolicy" in data:
        import capo_cloudhsm_v2.types.backup_retention_policy

        out["backup_retention_policy"] = (
            capo_cloudhsm_v2.types.backup_retention_policy.deserialize_aws_json_1_1(
                data["BackupRetentionPolicy"]
            )
        )
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "CreateTimestamp" in data:
        import capo_cloudhsm_v2.types.timestamp

        out["create_timestamp"] = (
            capo_cloudhsm_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if "Hsms" in data:
        import capo_cloudhsm_v2.types.hsms

        out["hsms"] = capo_cloudhsm_v2.types.hsms.deserialize_aws_json_1_1(data["Hsms"])
    if "HsmType" in data:
        out["hsm_type"] = data["HsmType"]
    if "HsmTypeRollbackExpiration" in data:
        import capo_cloudhsm_v2.types.timestamp

        out["hsm_type_rollback_expiration"] = (
            capo_cloudhsm_v2.types.timestamp.deserialize_aws_json_1_1(
                data["HsmTypeRollbackExpiration"]
            )
        )
    if "PreCoPassword" in data:
        out["pre_co_password"] = data["PreCoPassword"]
    if "SecurityGroup" in data:
        out["security_group"] = data["SecurityGroup"]
    if "SourceBackupId" in data:
        out["source_backup_id"] = data["SourceBackupId"]
    if "State" in data:
        import capo_cloudhsm_v2.types.cluster_state

        out["state"] = capo_cloudhsm_v2.types.cluster_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateMessage" in data:
        out["state_message"] = data["StateMessage"]
    if "SubnetMapping" in data:
        import capo_cloudhsm_v2.types.external_subnet_mapping

        out["subnet_mapping"] = (
            capo_cloudhsm_v2.types.external_subnet_mapping.deserialize_aws_json_1_1(
                data["SubnetMapping"]
            )
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "NetworkType" in data:
        import capo_cloudhsm_v2.types.network_type

        out["network_type"] = (
            capo_cloudhsm_v2.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    if "Certificates" in data:
        import capo_cloudhsm_v2.types.certificates

        out["certificates"] = (
            capo_cloudhsm_v2.types.certificates.deserialize_aws_json_1_1(
                data["Certificates"]
            )
        )
    if "TagList" in data:
        import capo_cloudhsm_v2.types.tag_list

        out["tag_list"] = capo_cloudhsm_v2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    if "Mode" in data:
        import capo_cloudhsm_v2.types.cluster_mode

        out["mode"] = capo_cloudhsm_v2.types.cluster_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    return out

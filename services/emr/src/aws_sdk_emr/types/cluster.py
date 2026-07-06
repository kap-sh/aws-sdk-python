"""Generated from Smithy shape ``com.amazonaws.emr#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.application_list
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.cluster_status
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.ec2_instance_attributes
    import aws_sdk_emr.types.instance_collection_type
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.kerberos_attributes
    import aws_sdk_emr.types.monitoring_configuration
    import aws_sdk_emr.types.optional_arn_type
    import aws_sdk_emr.types.placement_group_config_list
    import aws_sdk_emr.types.repo_upgrade_on_boot
    import aws_sdk_emr.types.scale_down_behavior
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class Cluster(TypedDict, closed=True):
    id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The unique identifier for the cluster.</p>"""
    name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name of the cluster. This parameter can't contain the characters <, >, $, |, or ` (backtick).</p>"""
    status: NotRequired["aws_sdk_emr.types.cluster_status.ClusterStatus"]
    """<p>The current status details about the cluster.</p>"""
    ec2_instance_attributes: NotRequired[
        "aws_sdk_emr.types.ec2_instance_attributes.Ec2InstanceAttributes"
    ]
    """<p>Provides information about the Amazon EC2 instances in a cluster grouped by category. For example, key name, subnet ID, IAM instance profile, and so on.</p>"""
    instance_collection_type: NotRequired[
        "aws_sdk_emr.types.instance_collection_type.InstanceCollectionType"
    ]
    """<note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note> <p>The instance group configuration of the cluster. A value of <code>INSTANCE_GROUP</code> indicates a uniform instance group configuration. A value of <code>INSTANCE_FLEET</code> indicates an instance fleets configuration.</p>"""
    log_uri: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The path to the Amazon S3 location where logs for this cluster are stored.</p>"""
    log_encryption_kms_key_id: NotRequired["aws_sdk_emr.types.string.String"]
    """<p> The KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0. </p>"""
    requested_ami_version: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The AMI version requested for this cluster.</p>"""
    running_ami_version: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The AMI version running on this cluster.</p>"""
    release_label: NotRequired["aws_sdk_emr.types.string.String"]
    r"""<p>The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form <code>emr-x.x.x</code>, where x.x.x is an Amazon EMR release version such as <code>emr-5.14.0</code>. For more information about Amazon EMR release versions and included application versions and features, see <a href=\"https://docs.aws.amazon.com/emr/latest/ReleaseGuide/\">https://docs.aws.amazon.com/emr/latest/ReleaseGuide/</a>. The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use <code>AmiVersion</code>.</p>"""
    auto_terminate: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Specifies whether the cluster should terminate after completing all steps.</p>"""
    termination_protected: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Indicates whether Amazon EMR will lock the cluster to prevent the Amazon EC2 instances from being terminated by an API call or user intervention, or in the event of a cluster error.</p>"""
    unhealthy_node_replacement: NotRequired[
        "aws_sdk_emr.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether Amazon EMR should gracefully replace Amazon EC2 core instances that have degraded within the cluster.</p>"""
    visible_to_all_users: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    r"""<p>Indicates whether the cluster is visible to IAM principals in the Amazon Web Services account associated with the cluster. When <code>true</code>, IAM principals in the Amazon Web Services account can perform Amazon EMR cluster actions on the cluster that their IAM policies allow. When <code>false</code>, only the IAM principal that created the cluster and the Amazon Web Services account root user can perform Amazon EMR actions, regardless of IAM permissions policies attached to other IAM principals.</p> <p>The default value is <code>true</code> if a value is not provided when creating a cluster using the Amazon EMR API <a>RunJobFlow</a> command, the CLI <a href=\"https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html\">create-cluster</a> command, or the Amazon Web Services Management Console.</p>"""
    applications: NotRequired["aws_sdk_emr.types.application_list.ApplicationList"]
    """<p>The applications installed on this cluster.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>A list of tags associated with a cluster.</p>"""
    service_role: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The IAM role that Amazon EMR assumes in order to access Amazon Web Services resources on your behalf.</p>"""
    normalized_instance_hours: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.</p>"""
    master_public_dns_name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.</p>"""
    security_configuration: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration applied to the cluster.</p>"""
    auto_scaling_role: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>An IAM role for automatic scaling policies. The default role is <code>EMR_AutoScaling_DefaultRole</code>. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.</p>"""
    scale_down_behavior: NotRequired[
        "aws_sdk_emr.types.scale_down_behavior.ScaleDownBehavior"
    ]
    """<p>The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. <code>TERMINATE_AT_INSTANCE_HOUR</code> indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. <code>TERMINATE_AT_TASK_COMPLETION</code> indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. <code>TERMINATE_AT_TASK_COMPLETION</code> is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.</p>"""
    custom_ami_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.</p>"""
    ebs_root_volume_size: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.</p>"""
    repo_upgrade_on_boot: NotRequired[
        "aws_sdk_emr.types.repo_upgrade_on_boot.RepoUpgradeOnBoot"
    ]
    """<p>Applies only when <code>CustomAmiID</code> is used. Specifies the type of updates that the Amazon Linux AMI package repositories apply when an instance boots using the AMI.</p>"""
    kerberos_attributes: NotRequired[
        "aws_sdk_emr.types.kerberos_attributes.KerberosAttributes"
    ]
    r"""<p>Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see <a href=\"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html\">Use Kerberos Authentication</a> in the <i>Amazon EMR Management Guide</i>.</p>"""
    cluster_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name of the cluster.</p>"""
    outpost_arn: NotRequired["aws_sdk_emr.types.optional_arn_type.OptionalArnType"]
    """<p> The Amazon Resource Name (ARN) of the Outpost where the cluster is launched. </p>"""
    step_concurrency_level: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>Specifies the number of steps that can be executed concurrently.</p>"""
    placement_groups: NotRequired[
        "aws_sdk_emr.types.placement_group_config_list.PlacementGroupConfigList"
    ]
    """<p>Placement group configured for an Amazon EMR cluster.</p>"""
    os_release_label: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The Amazon Linux release specified in a cluster launch RunJobFlow request. If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.</p>"""
    ebs_root_volume_iops: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>"""
    ebs_root_volume_throughput: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>"""
    extended_support: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Reserved.</p>"""
    monitoring_configuration: NotRequired[
        "aws_sdk_emr.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Contains Cloudwatch log configuration metadata and settings.</p>"""
    session_enabled: NotRequired["aws_sdk_emr.types.boolean_object.BooleanObject"]
    """<p>Indicates whether Spark Connect sessions are enabled on the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cluster) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_emr.types.cluster_status

        out["Status"] = aws_sdk_emr.types.cluster_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "ec2_instance_attributes" in value:
        import aws_sdk_emr.types.ec2_instance_attributes

        out["Ec2InstanceAttributes"] = (
            aws_sdk_emr.types.ec2_instance_attributes.serialize_aws_json_1_1(
                value["ec2_instance_attributes"]
            )
        )
    if "instance_collection_type" in value:
        import aws_sdk_emr.types.instance_collection_type

        out["InstanceCollectionType"] = (
            aws_sdk_emr.types.instance_collection_type.serialize_aws_json_1_1(
                value["instance_collection_type"]
            )
        )
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "log_encryption_kms_key_id" in value:
        out["LogEncryptionKmsKeyId"] = value["log_encryption_kms_key_id"]
    if "requested_ami_version" in value:
        out["RequestedAmiVersion"] = value["requested_ami_version"]
    if "running_ami_version" in value:
        out["RunningAmiVersion"] = value["running_ami_version"]
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "auto_terminate" in value:
        out["AutoTerminate"] = value["auto_terminate"]
    if "termination_protected" in value:
        out["TerminationProtected"] = value["termination_protected"]
    if "unhealthy_node_replacement" in value:
        out["UnhealthyNodeReplacement"] = value["unhealthy_node_replacement"]
    if "visible_to_all_users" in value:
        out["VisibleToAllUsers"] = value["visible_to_all_users"]
    if "applications" in value:
        import aws_sdk_emr.types.application_list

        out["Applications"] = aws_sdk_emr.types.application_list.serialize_aws_json_1_1(
            value["applications"]
        )
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "normalized_instance_hours" in value:
        out["NormalizedInstanceHours"] = value["normalized_instance_hours"]
    if "master_public_dns_name" in value:
        out["MasterPublicDnsName"] = value["master_public_dns_name"]
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "auto_scaling_role" in value:
        out["AutoScalingRole"] = value["auto_scaling_role"]
    if "scale_down_behavior" in value:
        import aws_sdk_emr.types.scale_down_behavior

        out["ScaleDownBehavior"] = (
            aws_sdk_emr.types.scale_down_behavior.serialize_aws_json_1_1(
                value["scale_down_behavior"]
            )
        )
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    if "ebs_root_volume_size" in value:
        out["EbsRootVolumeSize"] = value["ebs_root_volume_size"]
    if "repo_upgrade_on_boot" in value:
        import aws_sdk_emr.types.repo_upgrade_on_boot

        out["RepoUpgradeOnBoot"] = (
            aws_sdk_emr.types.repo_upgrade_on_boot.serialize_aws_json_1_1(
                value["repo_upgrade_on_boot"]
            )
        )
    if "kerberos_attributes" in value:
        import aws_sdk_emr.types.kerberos_attributes

        out["KerberosAttributes"] = (
            aws_sdk_emr.types.kerberos_attributes.serialize_aws_json_1_1(
                value["kerberos_attributes"]
            )
        )
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "step_concurrency_level" in value:
        out["StepConcurrencyLevel"] = value["step_concurrency_level"]
    if "placement_groups" in value:
        import aws_sdk_emr.types.placement_group_config_list

        out["PlacementGroups"] = (
            aws_sdk_emr.types.placement_group_config_list.serialize_aws_json_1_1(
                value["placement_groups"]
            )
        )
    if "os_release_label" in value:
        out["OSReleaseLabel"] = value["os_release_label"]
    if "ebs_root_volume_iops" in value:
        out["EbsRootVolumeIops"] = value["ebs_root_volume_iops"]
    if "ebs_root_volume_throughput" in value:
        out["EbsRootVolumeThroughput"] = value["ebs_root_volume_throughput"]
    if "extended_support" in value:
        out["ExtendedSupport"] = value["extended_support"]
    if "monitoring_configuration" in value:
        import aws_sdk_emr.types.monitoring_configuration

        out["MonitoringConfiguration"] = (
            aws_sdk_emr.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "session_enabled" in value:
        out["SessionEnabled"] = value["session_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_emr.types.cluster_status

        out["status"] = aws_sdk_emr.types.cluster_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Ec2InstanceAttributes" in data:
        import aws_sdk_emr.types.ec2_instance_attributes

        out["ec2_instance_attributes"] = (
            aws_sdk_emr.types.ec2_instance_attributes.deserialize_aws_json_1_1(
                data["Ec2InstanceAttributes"]
            )
        )
    if "InstanceCollectionType" in data:
        import aws_sdk_emr.types.instance_collection_type

        out["instance_collection_type"] = (
            aws_sdk_emr.types.instance_collection_type.deserialize_aws_json_1_1(
                data["InstanceCollectionType"]
            )
        )
    if "LogUri" in data:
        out["log_uri"] = data["LogUri"]
    if "LogEncryptionKmsKeyId" in data:
        out["log_encryption_kms_key_id"] = data["LogEncryptionKmsKeyId"]
    if "RequestedAmiVersion" in data:
        out["requested_ami_version"] = data["RequestedAmiVersion"]
    if "RunningAmiVersion" in data:
        out["running_ami_version"] = data["RunningAmiVersion"]
    if "ReleaseLabel" in data:
        out["release_label"] = data["ReleaseLabel"]
    if "AutoTerminate" in data:
        out["auto_terminate"] = data["AutoTerminate"]
    if "TerminationProtected" in data:
        out["termination_protected"] = data["TerminationProtected"]
    if "UnhealthyNodeReplacement" in data:
        out["unhealthy_node_replacement"] = data["UnhealthyNodeReplacement"]
    if "VisibleToAllUsers" in data:
        out["visible_to_all_users"] = data["VisibleToAllUsers"]
    if "Applications" in data:
        import aws_sdk_emr.types.application_list

        out["applications"] = (
            aws_sdk_emr.types.application_list.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "NormalizedInstanceHours" in data:
        out["normalized_instance_hours"] = data["NormalizedInstanceHours"]
    if "MasterPublicDnsName" in data:
        out["master_public_dns_name"] = data["MasterPublicDnsName"]
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "SecurityConfiguration" in data:
        out["security_configuration"] = data["SecurityConfiguration"]
    if "AutoScalingRole" in data:
        out["auto_scaling_role"] = data["AutoScalingRole"]
    if "ScaleDownBehavior" in data:
        import aws_sdk_emr.types.scale_down_behavior

        out["scale_down_behavior"] = (
            aws_sdk_emr.types.scale_down_behavior.deserialize_aws_json_1_1(
                data["ScaleDownBehavior"]
            )
        )
    if "CustomAmiId" in data:
        out["custom_ami_id"] = data["CustomAmiId"]
    if "EbsRootVolumeSize" in data:
        out["ebs_root_volume_size"] = data["EbsRootVolumeSize"]
    if "RepoUpgradeOnBoot" in data:
        import aws_sdk_emr.types.repo_upgrade_on_boot

        out["repo_upgrade_on_boot"] = (
            aws_sdk_emr.types.repo_upgrade_on_boot.deserialize_aws_json_1_1(
                data["RepoUpgradeOnBoot"]
            )
        )
    if "KerberosAttributes" in data:
        import aws_sdk_emr.types.kerberos_attributes

        out["kerberos_attributes"] = (
            aws_sdk_emr.types.kerberos_attributes.deserialize_aws_json_1_1(
                data["KerberosAttributes"]
            )
        )
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    if "StepConcurrencyLevel" in data:
        out["step_concurrency_level"] = data["StepConcurrencyLevel"]
    if "PlacementGroups" in data:
        import aws_sdk_emr.types.placement_group_config_list

        out["placement_groups"] = (
            aws_sdk_emr.types.placement_group_config_list.deserialize_aws_json_1_1(
                data["PlacementGroups"]
            )
        )
    if "OSReleaseLabel" in data:
        out["os_release_label"] = data["OSReleaseLabel"]
    if "EbsRootVolumeIops" in data:
        out["ebs_root_volume_iops"] = data["EbsRootVolumeIops"]
    if "EbsRootVolumeThroughput" in data:
        out["ebs_root_volume_throughput"] = data["EbsRootVolumeThroughput"]
    if "ExtendedSupport" in data:
        out["extended_support"] = data["ExtendedSupport"]
    if "MonitoringConfiguration" in data:
        import aws_sdk_emr.types.monitoring_configuration

        out["monitoring_configuration"] = (
            aws_sdk_emr.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if "SessionEnabled" in data:
        out["session_enabled"] = data["SessionEnabled"]
    return out

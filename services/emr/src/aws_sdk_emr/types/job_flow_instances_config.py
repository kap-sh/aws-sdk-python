"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowInstancesConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.boolean
    import aws_sdk_emr.types.boolean_object
    import aws_sdk_emr.types.instance_fleet_config_list
    import aws_sdk_emr.types.instance_group_config_list
    import aws_sdk_emr.types.instance_type
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.placement_type
    import aws_sdk_emr.types.security_groups_list
    import aws_sdk_emr.types.xml_string_max_len256
    import aws_sdk_emr.types.xml_string_max_len256_list


class JobFlowInstancesConfig(TypedDict):
    master_instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type of the master node.</p>"""
    slave_instance_type: NotRequired["aws_sdk_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type of the core and task nodes.</p>"""
    instance_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>The number of Amazon EC2 instances in the cluster.</p>"""
    instance_groups: NotRequired[
        "aws_sdk_emr.types.instance_group_config_list.InstanceGroupConfigList"
    ]
    """<p>Configuration for the instance groups in a cluster.</p>"""
    instance_fleets: NotRequired[
        "aws_sdk_emr.types.instance_fleet_config_list.InstanceFleetConfigList"
    ]
    """<note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note> <p>Describes the Amazon EC2 instances and instance configurations for clusters that use the instance fleet configuration.</p>"""
    ec2_key_name: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    r"""<p>The name of the Amazon EC2 key pair that can be used to connect to the master node using SSH as the user called \"hadoop.\"</p>"""
    placement: NotRequired["aws_sdk_emr.types.placement_type.PlacementType"]
    """<p>The Availability Zone in which the cluster runs.</p>"""
    keep_job_flow_alive_when_no_steps: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    r"""<p>Specifies whether the cluster should remain available after completing all steps. Defaults to <code>false</code>. For more information about configuring cluster termination, see <a href=\"https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html\">Control Cluster Termination</a> in the <i>EMR Management Guide</i>.</p>"""
    termination_protected: NotRequired["aws_sdk_emr.types.boolean.Boolean"]
    """<p>Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.</p>"""
    unhealthy_node_replacement: NotRequired[
        "aws_sdk_emr.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.</p>"""
    hadoop_version: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    r"""<p>Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are \"0.18\" (no longer maintained), \"0.20\" (no longer maintained), \"0.20.205\" (no longer maintained), \"1.0.3\", \"2.2.0\", or \"2.4.0\". If you do not set this value, the default of 0.18 is used, unless the <code>AmiVersion</code> parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.</p>"""
    ec2_subnet_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.</p>"""
    ec2_subnet_ids: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256_list.XmlStringMaxLen256List"
    ]
    """<p>Applies to clusters that use the instance fleet configuration. When multiple Amazon EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note>"""
    emr_managed_master_security_group: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier of the Amazon EC2 security group for the master node. If you specify <code>EmrManagedMasterSecurityGroup</code>, you must also specify <code>EmrManagedSlaveSecurityGroup</code>.</p>"""
    emr_managed_slave_security_group: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier of the Amazon EC2 security group for the core and task nodes. If you specify <code>EmrManagedSlaveSecurityGroup</code>, you must also specify <code>EmrManagedMasterSecurityGroup</code>.</p>"""
    service_access_security_group: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.</p>"""
    additional_master_security_groups: NotRequired[
        "aws_sdk_emr.types.security_groups_list.SecurityGroupsList"
    ]
    """<p>A list of additional Amazon EC2 security group IDs for the master node.</p>"""
    additional_slave_security_groups: NotRequired[
        "aws_sdk_emr.types.security_groups_list.SecurityGroupsList"
    ]
    """<p>A list of additional Amazon EC2 security group IDs for the core and task nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowInstancesConfig) -> dict:
    out: dict = {}
    if "master_instance_type" in value:
        out["MasterInstanceType"] = value["master_instance_type"]
    if "slave_instance_type" in value:
        out["SlaveInstanceType"] = value["slave_instance_type"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_groups" in value:
        import aws_sdk_emr.types.instance_group_config_list

        out["InstanceGroups"] = (
            aws_sdk_emr.types.instance_group_config_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "instance_fleets" in value:
        import aws_sdk_emr.types.instance_fleet_config_list

        out["InstanceFleets"] = (
            aws_sdk_emr.types.instance_fleet_config_list.serialize_aws_json_1_1(
                value["instance_fleets"]
            )
        )
    if "ec2_key_name" in value:
        out["Ec2KeyName"] = value["ec2_key_name"]
    if "placement" in value:
        import aws_sdk_emr.types.placement_type

        out["Placement"] = aws_sdk_emr.types.placement_type.serialize_aws_json_1_1(
            value["placement"]
        )
    if "keep_job_flow_alive_when_no_steps" in value:
        out["KeepJobFlowAliveWhenNoSteps"] = value["keep_job_flow_alive_when_no_steps"]
    if "termination_protected" in value:
        out["TerminationProtected"] = value["termination_protected"]
    if "unhealthy_node_replacement" in value:
        out["UnhealthyNodeReplacement"] = value["unhealthy_node_replacement"]
    if "hadoop_version" in value:
        out["HadoopVersion"] = value["hadoop_version"]
    if "ec2_subnet_id" in value:
        out["Ec2SubnetId"] = value["ec2_subnet_id"]
    if "ec2_subnet_ids" in value:
        import aws_sdk_emr.types.xml_string_max_len256_list

        out["Ec2SubnetIds"] = (
            aws_sdk_emr.types.xml_string_max_len256_list.serialize_aws_json_1_1(
                value["ec2_subnet_ids"]
            )
        )
    if "emr_managed_master_security_group" in value:
        out["EmrManagedMasterSecurityGroup"] = value[
            "emr_managed_master_security_group"
        ]
    if "emr_managed_slave_security_group" in value:
        out["EmrManagedSlaveSecurityGroup"] = value["emr_managed_slave_security_group"]
    if "service_access_security_group" in value:
        out["ServiceAccessSecurityGroup"] = value["service_access_security_group"]
    if "additional_master_security_groups" in value:
        import aws_sdk_emr.types.security_groups_list

        out["AdditionalMasterSecurityGroups"] = (
            aws_sdk_emr.types.security_groups_list.serialize_aws_json_1_1(
                value["additional_master_security_groups"]
            )
        )
    if "additional_slave_security_groups" in value:
        import aws_sdk_emr.types.security_groups_list

        out["AdditionalSlaveSecurityGroups"] = (
            aws_sdk_emr.types.security_groups_list.serialize_aws_json_1_1(
                value["additional_slave_security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobFlowInstancesConfig:
    out: JobFlowInstancesConfig = {}  # type: ignore[typeddict-item]
    if "MasterInstanceType" in data:
        out["master_instance_type"] = data["MasterInstanceType"]
    if "SlaveInstanceType" in data:
        out["slave_instance_type"] = data["SlaveInstanceType"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "InstanceGroups" in data:
        import aws_sdk_emr.types.instance_group_config_list

        out["instance_groups"] = (
            aws_sdk_emr.types.instance_group_config_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "InstanceFleets" in data:
        import aws_sdk_emr.types.instance_fleet_config_list

        out["instance_fleets"] = (
            aws_sdk_emr.types.instance_fleet_config_list.deserialize_aws_json_1_1(
                data["InstanceFleets"]
            )
        )
    if "Ec2KeyName" in data:
        out["ec2_key_name"] = data["Ec2KeyName"]
    if "Placement" in data:
        import aws_sdk_emr.types.placement_type

        out["placement"] = aws_sdk_emr.types.placement_type.deserialize_aws_json_1_1(
            data["Placement"]
        )
    if "KeepJobFlowAliveWhenNoSteps" in data:
        out["keep_job_flow_alive_when_no_steps"] = data["KeepJobFlowAliveWhenNoSteps"]
    if "TerminationProtected" in data:
        out["termination_protected"] = data["TerminationProtected"]
    if "UnhealthyNodeReplacement" in data:
        out["unhealthy_node_replacement"] = data["UnhealthyNodeReplacement"]
    if "HadoopVersion" in data:
        out["hadoop_version"] = data["HadoopVersion"]
    if "Ec2SubnetId" in data:
        out["ec2_subnet_id"] = data["Ec2SubnetId"]
    if "Ec2SubnetIds" in data:
        import aws_sdk_emr.types.xml_string_max_len256_list

        out["ec2_subnet_ids"] = (
            aws_sdk_emr.types.xml_string_max_len256_list.deserialize_aws_json_1_1(
                data["Ec2SubnetIds"]
            )
        )
    if "EmrManagedMasterSecurityGroup" in data:
        out["emr_managed_master_security_group"] = data["EmrManagedMasterSecurityGroup"]
    if "EmrManagedSlaveSecurityGroup" in data:
        out["emr_managed_slave_security_group"] = data["EmrManagedSlaveSecurityGroup"]
    if "ServiceAccessSecurityGroup" in data:
        out["service_access_security_group"] = data["ServiceAccessSecurityGroup"]
    if "AdditionalMasterSecurityGroups" in data:
        import aws_sdk_emr.types.security_groups_list

        out["additional_master_security_groups"] = (
            aws_sdk_emr.types.security_groups_list.deserialize_aws_json_1_1(
                data["AdditionalMasterSecurityGroups"]
            )
        )
    if "AdditionalSlaveSecurityGroups" in data:
        import aws_sdk_emr.types.security_groups_list

        out["additional_slave_security_groups"] = (
            aws_sdk_emr.types.security_groups_list.deserialize_aws_json_1_1(
                data["AdditionalSlaveSecurityGroups"]
            )
        )
    return out

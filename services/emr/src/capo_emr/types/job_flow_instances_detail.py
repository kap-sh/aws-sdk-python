"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowInstancesDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.boolean_object
    import capo_emr.types.instance_group_detail_list
    import capo_emr.types.instance_type
    import capo_emr.types.integer
    import capo_emr.types.placement_type
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256


class JobFlowInstancesDetail(TypedDict, closed=True):
    master_instance_type: NotRequired["capo_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 master node instance type.</p>"""
    master_public_dns_name: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.</p>"""
    master_instance_id: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The Amazon EC2 instance identifier of the master node.</p>"""
    slave_instance_type: NotRequired["capo_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 core and task node instance type.</p>"""
    instance_count: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The number of Amazon EC2 instances in the cluster. If the value is 1, the same instance serves as both the master and core and task node. If the value is greater than 1, one instance is the master node and all others are core and task nodes.</p>"""
    instance_groups: NotRequired[
        "capo_emr.types.instance_group_detail_list.InstanceGroupDetailList"
    ]
    """<p>Details about the instance groups in a cluster.</p>"""
    normalized_instance_hours: NotRequired["capo_emr.types.integer.Integer"]
    """<p>An approximation of the cost of the cluster, represented in m1.small/hours. This value is increased one time for every hour that an m1.small instance runs. Larger instances are weighted more heavily, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being increased incrementally four times. This result is only an approximation and does not reflect the actual billing rate.</p>"""
    ec2_key_name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of an Amazon EC2 key pair that can be used to connect to the master node using SSH.</p>"""
    ec2_subnet_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>For clusters launched within Amazon Virtual Private Cloud, this is the identifier of the subnet where the cluster was launched.</p>"""
    placement: NotRequired["capo_emr.types.placement_type.PlacementType"]
    """<p>The Amazon EC2 Availability Zone for the cluster.</p>"""
    keep_job_flow_alive_when_no_steps: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Specifies whether the cluster should remain available after completing all steps.</p>"""
    termination_protected: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Specifies whether the Amazon EC2 instances in the cluster are protected from termination by API calls, user intervention, or in the event of a job-flow error.</p>"""
    unhealthy_node_replacement: NotRequired[
        "capo_emr.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.</p>"""
    hadoop_version: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Hadoop version for the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowInstancesDetail) -> dict:
    out: dict = {}
    if "master_instance_type" in value:
        out["MasterInstanceType"] = value["master_instance_type"]
    if "master_public_dns_name" in value:
        out["MasterPublicDnsName"] = value["master_public_dns_name"]
    if "master_instance_id" in value:
        out["MasterInstanceId"] = value["master_instance_id"]
    if "slave_instance_type" in value:
        out["SlaveInstanceType"] = value["slave_instance_type"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_groups" in value:
        import capo_emr.types.instance_group_detail_list

        out["InstanceGroups"] = (
            capo_emr.types.instance_group_detail_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "normalized_instance_hours" in value:
        out["NormalizedInstanceHours"] = value["normalized_instance_hours"]
    if "ec2_key_name" in value:
        out["Ec2KeyName"] = value["ec2_key_name"]
    if "ec2_subnet_id" in value:
        out["Ec2SubnetId"] = value["ec2_subnet_id"]
    if "placement" in value:
        import capo_emr.types.placement_type

        out["Placement"] = capo_emr.types.placement_type.serialize_aws_json_1_1(
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
    return out


def deserialize_aws_json_1_1(data: dict) -> JobFlowInstancesDetail:
    out: JobFlowInstancesDetail = {}  # type: ignore[typeddict-item]
    if "MasterInstanceType" in data:
        out["master_instance_type"] = data["MasterInstanceType"]
    if "MasterPublicDnsName" in data:
        out["master_public_dns_name"] = data["MasterPublicDnsName"]
    if "MasterInstanceId" in data:
        out["master_instance_id"] = data["MasterInstanceId"]
    if "SlaveInstanceType" in data:
        out["slave_instance_type"] = data["SlaveInstanceType"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "InstanceGroups" in data:
        import capo_emr.types.instance_group_detail_list

        out["instance_groups"] = (
            capo_emr.types.instance_group_detail_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "NormalizedInstanceHours" in data:
        out["normalized_instance_hours"] = data["NormalizedInstanceHours"]
    if "Ec2KeyName" in data:
        out["ec2_key_name"] = data["Ec2KeyName"]
    if "Ec2SubnetId" in data:
        out["ec2_subnet_id"] = data["Ec2SubnetId"]
    if "Placement" in data:
        import capo_emr.types.placement_type

        out["placement"] = capo_emr.types.placement_type.deserialize_aws_json_1_1(
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
    return out

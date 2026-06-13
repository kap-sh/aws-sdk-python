"""Generated from Smithy shape ``com.amazonaws.emr#AddInstanceGroupsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.instance_group_ids_list
    import aws_sdk_emr.types.xml_string_max_len256


class AddInstanceGroupsOutput(TypedDict):
    job_flow_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The job flow ID in which the instance groups are added.</p>"""
    instance_group_ids: NotRequired[
        "aws_sdk_emr.types.instance_group_ids_list.InstanceGroupIdsList"
    ]
    """<p>Instance group IDs of the newly created instance groups.</p>"""
    cluster_arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name of the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddInstanceGroupsOutput) -> dict:
    out: dict = {}
    if "job_flow_id" in value:
        out["JobFlowId"] = value["job_flow_id"]
    if "instance_group_ids" in value:
        import aws_sdk_emr.types.instance_group_ids_list

        out["InstanceGroupIds"] = (
            aws_sdk_emr.types.instance_group_ids_list.serialize_aws_json_1_1(
                value["instance_group_ids"]
            )
        )
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddInstanceGroupsOutput:
    out: AddInstanceGroupsOutput = {}  # type: ignore[typeddict-item]
    if "JobFlowId" in data:
        out["job_flow_id"] = data["JobFlowId"]
    if "InstanceGroupIds" in data:
        import aws_sdk_emr.types.instance_group_ids_list

        out["instance_group_ids"] = (
            aws_sdk_emr.types.instance_group_ids_list.deserialize_aws_json_1_1(
                data["InstanceGroupIds"]
            )
        )
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out

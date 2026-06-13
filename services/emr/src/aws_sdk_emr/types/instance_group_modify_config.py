"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupModifyConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.ec2_instance_ids_to_terminate_list
    import aws_sdk_emr.types.integer
    import aws_sdk_emr.types.reconfiguration_type
    import aws_sdk_emr.types.shrink_policy
    import aws_sdk_emr.types.xml_string_max_len256


class InstanceGroupModifyConfig(TypedDict):
    instance_group_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Unique ID of the instance group to modify.</p>"""
    instance_count: NotRequired["aws_sdk_emr.types.integer.Integer"]
    """<p>Target size for the instance group.</p>"""
    ec2_instance_ids_to_terminate: NotRequired[
        "aws_sdk_emr.types.ec2_instance_ids_to_terminate_list.EC2InstanceIdsToTerminateList"
    ]
    """<p>The Amazon EC2 InstanceIds to terminate. After you terminate the instances, the instance group will not return to its original requested size.</p>"""
    shrink_policy: NotRequired["aws_sdk_emr.types.shrink_policy.ShrinkPolicy"]
    """<p>Policy for customizing shrink operations.</p>"""
    reconfiguration_type: NotRequired[
        "aws_sdk_emr.types.reconfiguration_type.ReconfigurationType"
    ]
    """<p>Type of reconfiguration requested. Valid values are MERGE and OVERWRITE.</p>"""
    configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>A list of new or modified configurations to apply for an instance group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupModifyConfig) -> dict:
    out: dict = {}
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "ec2_instance_ids_to_terminate" in value:
        import aws_sdk_emr.types.ec2_instance_ids_to_terminate_list

        out["EC2InstanceIdsToTerminate"] = (
            aws_sdk_emr.types.ec2_instance_ids_to_terminate_list.serialize_aws_json_1_1(
                value["ec2_instance_ids_to_terminate"]
            )
        )
    if "shrink_policy" in value:
        import aws_sdk_emr.types.shrink_policy

        out["ShrinkPolicy"] = aws_sdk_emr.types.shrink_policy.serialize_aws_json_1_1(
            value["shrink_policy"]
        )
    if "reconfiguration_type" in value:
        import aws_sdk_emr.types.reconfiguration_type

        out["ReconfigurationType"] = (
            aws_sdk_emr.types.reconfiguration_type.serialize_aws_json_1_1(
                value["reconfiguration_type"]
            )
        )
    if "configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["Configurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupModifyConfig:
    out: InstanceGroupModifyConfig = {}  # type: ignore[typeddict-item]
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "EC2InstanceIdsToTerminate" in data:
        import aws_sdk_emr.types.ec2_instance_ids_to_terminate_list

        out["ec2_instance_ids_to_terminate"] = (
            aws_sdk_emr.types.ec2_instance_ids_to_terminate_list.deserialize_aws_json_1_1(
                data["EC2InstanceIdsToTerminate"]
            )
        )
    if "ShrinkPolicy" in data:
        import aws_sdk_emr.types.shrink_policy

        out["shrink_policy"] = aws_sdk_emr.types.shrink_policy.deserialize_aws_json_1_1(
            data["ShrinkPolicy"]
        )
    if "ReconfigurationType" in data:
        import aws_sdk_emr.types.reconfiguration_type

        out["reconfiguration_type"] = (
            aws_sdk_emr.types.reconfiguration_type.deserialize_aws_json_1_1(
                data["ReconfigurationType"]
            )
        )
    if "Configurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.emr#ModifyInstanceGroupsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.instance_group_modify_config_list


class ModifyInstanceGroupsInput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster to which the instance group belongs.</p>"""
    instance_groups: NotRequired[
        "aws_sdk_emr.types.instance_group_modify_config_list.InstanceGroupModifyConfigList"
    ]
    """<p>Instance groups to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyInstanceGroupsInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_groups" in value:
        import aws_sdk_emr.types.instance_group_modify_config_list

        out["InstanceGroups"] = (
            aws_sdk_emr.types.instance_group_modify_config_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyInstanceGroupsInput:
    out: ModifyInstanceGroupsInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceGroups" in data:
        import aws_sdk_emr.types.instance_group_modify_config_list

        out["instance_groups"] = (
            aws_sdk_emr.types.instance_group_modify_config_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    return out

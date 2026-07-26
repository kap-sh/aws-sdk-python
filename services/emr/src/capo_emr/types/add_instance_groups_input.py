"""Generated from Smithy shape ``com.amazonaws.emr#AddInstanceGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_group_config_list
    import capo_emr.types.xml_string_max_len256


class AddInstanceGroupsInput(TypedDict, closed=True):
    instance_groups: NotRequired[
        "capo_emr.types.instance_group_config_list.InstanceGroupConfigList"
    ]
    """<p>Instance groups to add.</p>"""
    job_flow_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Job flow in which to add the instance groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddInstanceGroupsInput) -> dict:
    out: dict = {}
    if "instance_groups" in value:
        import capo_emr.types.instance_group_config_list

        out["InstanceGroups"] = (
            capo_emr.types.instance_group_config_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "job_flow_id" in value:
        out["JobFlowId"] = value["job_flow_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddInstanceGroupsInput:
    out: AddInstanceGroupsInput = {}  # type: ignore[typeddict-item]
    if "InstanceGroups" in data:
        import capo_emr.types.instance_group_config_list

        out["instance_groups"] = (
            capo_emr.types.instance_group_config_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if "JobFlowId" in data:
        out["job_flow_id"] = data["JobFlowId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.emr#InstanceResizePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.ec2_instance_ids_list
    import capo_emr.types.integer


class InstanceResizePolicy(TypedDict, closed=True):
    instances_to_terminate: NotRequired[
        "capo_emr.types.ec2_instance_ids_list.EC2InstanceIdsList"
    ]
    """<p>Specific list of instances to be terminated when shrinking an instance group.</p>"""
    instances_to_protect: NotRequired[
        "capo_emr.types.ec2_instance_ids_list.EC2InstanceIdsList"
    ]
    """<p>Specific list of instances to be protected when shrinking an instance group.</p>"""
    instance_termination_timeout: NotRequired["capo_emr.types.integer.Integer"]
    """<p>Decommissioning timeout override for the specific list of instances to be terminated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceResizePolicy) -> dict:
    out: dict = {}
    if "instances_to_terminate" in value:
        import capo_emr.types.ec2_instance_ids_list

        out["InstancesToTerminate"] = (
            capo_emr.types.ec2_instance_ids_list.serialize_aws_json_1_1(
                value["instances_to_terminate"]
            )
        )
    if "instances_to_protect" in value:
        import capo_emr.types.ec2_instance_ids_list

        out["InstancesToProtect"] = (
            capo_emr.types.ec2_instance_ids_list.serialize_aws_json_1_1(
                value["instances_to_protect"]
            )
        )
    if "instance_termination_timeout" in value:
        out["InstanceTerminationTimeout"] = value["instance_termination_timeout"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceResizePolicy:
    out: InstanceResizePolicy = {}  # type: ignore[typeddict-item]
    if "InstancesToTerminate" in data:
        import capo_emr.types.ec2_instance_ids_list

        out["instances_to_terminate"] = (
            capo_emr.types.ec2_instance_ids_list.deserialize_aws_json_1_1(
                data["InstancesToTerminate"]
            )
        )
    if "InstancesToProtect" in data:
        import capo_emr.types.ec2_instance_ids_list

        out["instances_to_protect"] = (
            capo_emr.types.ec2_instance_ids_list.deserialize_aws_json_1_1(
                data["InstancesToProtect"]
            )
        )
    if "InstanceTerminationTimeout" in data:
        out["instance_termination_timeout"] = data["InstanceTerminationTimeout"]
    return out

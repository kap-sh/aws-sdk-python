"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EC2InstanceErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ec2_instance_error

EC2InstanceErrors: TypeAlias = list[
    "capo_workspaces_instances.types.ec2_instance_error.EC2InstanceError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EC2InstanceErrors) -> list:
    import capo_workspaces_instances.types.ec2_instance_error

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.ec2_instance_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EC2InstanceErrors:
    import capo_workspaces_instances.types.ec2_instance_error

    out: EC2InstanceErrors = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.ec2_instance_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out

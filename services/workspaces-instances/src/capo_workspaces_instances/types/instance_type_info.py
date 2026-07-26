"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceTypeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.instance_type
    import capo_workspaces_instances.types.supported_instance_configurations


class InstanceTypeInfo(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_workspaces_instances.types.instance_type.InstanceType"
    ]
    """<p>Unique identifier for the WorkSpace Instance type.</p>"""
    supported_instance_configurations: NotRequired[
        "capo_workspaces_instances.types.supported_instance_configurations.SupportedInstanceConfigurations"
    ]
    """<p>Lists all valid combinations of tenancy, platform type, and billing mode supported for the specific WorkSpace Instance type. Contains the complete set of configuration options available for this instance type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypeInfo) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "supported_instance_configurations" in value:
        import capo_workspaces_instances.types.supported_instance_configurations

        out["SupportedInstanceConfigurations"] = (
            capo_workspaces_instances.types.supported_instance_configurations.serialize_aws_json_1_0(
                value["supported_instance_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceTypeInfo:
    out: InstanceTypeInfo = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "SupportedInstanceConfigurations" in data:
        import capo_workspaces_instances.types.supported_instance_configurations

        out["supported_instance_configurations"] = (
            capo_workspaces_instances.types.supported_instance_configurations.deserialize_aws_json_1_0(
                data["SupportedInstanceConfigurations"]
            )
        )
    return out

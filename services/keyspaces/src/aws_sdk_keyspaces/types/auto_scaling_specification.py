"""Generated from Smithy shape ``com.amazonaws.keyspaces#AutoScalingSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.auto_scaling_settings


class AutoScalingSpecification(TypedDict):
    write_capacity_auto_scaling: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_settings.AutoScalingSettings"
    ]
    """<p>The auto scaling settings for the table's write capacity.</p>"""
    read_capacity_auto_scaling: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_settings.AutoScalingSettings"
    ]
    """<p>The auto scaling settings for the table's read capacity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingSpecification) -> dict:
    out: dict = {}
    if "write_capacity_auto_scaling" in value:
        import aws_sdk_keyspaces.types.auto_scaling_settings

        out["writeCapacityAutoScaling"] = (
            aws_sdk_keyspaces.types.auto_scaling_settings.serialize_aws_json_1_0(
                value["write_capacity_auto_scaling"]
            )
        )
    if "read_capacity_auto_scaling" in value:
        import aws_sdk_keyspaces.types.auto_scaling_settings

        out["readCapacityAutoScaling"] = (
            aws_sdk_keyspaces.types.auto_scaling_settings.serialize_aws_json_1_0(
                value["read_capacity_auto_scaling"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingSpecification:
    out: AutoScalingSpecification = {}  # type: ignore[typeddict-item]
    if "writeCapacityAutoScaling" in data:
        import aws_sdk_keyspaces.types.auto_scaling_settings

        out["write_capacity_auto_scaling"] = (
            aws_sdk_keyspaces.types.auto_scaling_settings.deserialize_aws_json_1_0(
                data["writeCapacityAutoScaling"]
            )
        )
    if "readCapacityAutoScaling" in data:
        import aws_sdk_keyspaces.types.auto_scaling_settings

        out["read_capacity_auto_scaling"] = (
            aws_sdk_keyspaces.types.auto_scaling_settings.deserialize_aws_json_1_0(
                data["readCapacityAutoScaling"]
            )
        )
    return out

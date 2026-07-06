"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.auto_scaling_settings
    import aws_sdk_keyspaces.types.capacity_units
    import aws_sdk_keyspaces.types.region


class ReplicaSpecification(TypedDict, closed=True):
    region: "aws_sdk_keyspaces.types.region.region"
    """<p>The Amazon Web Services Region.</p>"""
    read_capacity_units: NotRequired[
        "aws_sdk_keyspaces.types.capacity_units.CapacityUnits"
    ]
    """<p>The provisioned read capacity units for the multi-Region table in the specified Amazon Web Services Region.</p>"""
    read_capacity_auto_scaling: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_settings.AutoScalingSettings"
    ]
    """<p>The read capacity auto scaling settings for the multi-Region table in the specified Amazon Web Services Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaSpecification) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    if "read_capacity_units" in value:
        out["readCapacityUnits"] = value["read_capacity_units"]
    if "read_capacity_auto_scaling" in value:
        import aws_sdk_keyspaces.types.auto_scaling_settings

        out["readCapacityAutoScaling"] = (
            aws_sdk_keyspaces.types.auto_scaling_settings.serialize_aws_json_1_0(
                value["read_capacity_auto_scaling"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaSpecification:
    out: ReplicaSpecification = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("ReplicaSpecification.region required")
    if "readCapacityUnits" in data:
        out["read_capacity_units"] = data["readCapacityUnits"]
    if "readCapacityAutoScaling" in data:
        import aws_sdk_keyspaces.types.auto_scaling_settings

        out["read_capacity_auto_scaling"] = (
            aws_sdk_keyspaces.types.auto_scaling_settings.deserialize_aws_json_1_0(
                data["readCapacityAutoScaling"]
            )
        )
    return out

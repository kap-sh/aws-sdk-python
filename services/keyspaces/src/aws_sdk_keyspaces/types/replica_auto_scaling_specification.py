"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaAutoScalingSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.auto_scaling_specification
    import aws_sdk_keyspaces.types.region


class ReplicaAutoScalingSpecification(TypedDict):
    region: NotRequired["aws_sdk_keyspaces.types.region.region"]
    """<p>The Amazon Web Services Region.</p>"""
    auto_scaling_specification: NotRequired[
        "aws_sdk_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
    ]
    """<p>The auto scaling settings for a multi-Region table in the specified Amazon Web Services Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingSpecification) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "auto_scaling_specification" in value:
        import aws_sdk_keyspaces.types.auto_scaling_specification

        out["autoScalingSpecification"] = (
            aws_sdk_keyspaces.types.auto_scaling_specification.serialize_aws_json_1_0(
                value["auto_scaling_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaAutoScalingSpecification:
    out: ReplicaAutoScalingSpecification = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    if "autoScalingSpecification" in data:
        import aws_sdk_keyspaces.types.auto_scaling_specification

        out["auto_scaling_specification"] = (
            aws_sdk_keyspaces.types.auto_scaling_specification.deserialize_aws_json_1_0(
                data["autoScalingSpecification"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CapacityUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.auto_scaling_update
    import aws_sdk_kafkaconnect.types.provisioned_capacity_update


class CapacityUpdate(TypedDict):
    auto_scaling: NotRequired[
        "aws_sdk_kafkaconnect.types.auto_scaling_update.AutoScalingUpdate"
    ]
    """<p>The target auto scaling setting.</p>"""
    provisioned_capacity: NotRequired[
        "aws_sdk_kafkaconnect.types.provisioned_capacity_update.ProvisionedCapacityUpdate"
    ]
    """<p>The target settings for provisioned capacity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityUpdate) -> dict:
    out: dict = {}
    if "auto_scaling" in value:
        import aws_sdk_kafkaconnect.types.auto_scaling_update

        out["autoScaling"] = (
            aws_sdk_kafkaconnect.types.auto_scaling_update.serialize_json(
                value["auto_scaling"]
            )
        )
    if "provisioned_capacity" in value:
        import aws_sdk_kafkaconnect.types.provisioned_capacity_update

        out["provisionedCapacity"] = (
            aws_sdk_kafkaconnect.types.provisioned_capacity_update.serialize_json(
                value["provisioned_capacity"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityUpdate:
    out: CapacityUpdate = {}  # type: ignore[typeddict-item]
    if "autoScaling" in data:
        import aws_sdk_kafkaconnect.types.auto_scaling_update

        out["auto_scaling"] = (
            aws_sdk_kafkaconnect.types.auto_scaling_update.deserialize_json(
                data["autoScaling"]
            )
        )
    if "provisionedCapacity" in data:
        import aws_sdk_kafkaconnect.types.provisioned_capacity_update

        out["provisioned_capacity"] = (
            aws_sdk_kafkaconnect.types.provisioned_capacity_update.deserialize_json(
                data["provisionedCapacity"]
            )
        )
    return out

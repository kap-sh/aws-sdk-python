"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CapacityUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.auto_scaling_update
    import capo_kafkaconnect.types.provisioned_capacity_update


class CapacityUpdate(TypedDict, closed=True):
    auto_scaling: NotRequired[
        "capo_kafkaconnect.types.auto_scaling_update.AutoScalingUpdate"
    ]
    """<p>The target auto scaling setting.</p>"""
    provisioned_capacity: NotRequired[
        "capo_kafkaconnect.types.provisioned_capacity_update.ProvisionedCapacityUpdate"
    ]
    """<p>The target settings for provisioned capacity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityUpdate) -> dict:
    out: dict = {}
    if "auto_scaling" in value:
        import capo_kafkaconnect.types.auto_scaling_update

        out["autoScaling"] = capo_kafkaconnect.types.auto_scaling_update.serialize_json(
            value["auto_scaling"]
        )
    if "provisioned_capacity" in value:
        import capo_kafkaconnect.types.provisioned_capacity_update

        out["provisionedCapacity"] = (
            capo_kafkaconnect.types.provisioned_capacity_update.serialize_json(
                value["provisioned_capacity"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityUpdate:
    out: CapacityUpdate = {}  # type: ignore[typeddict-item]
    if "autoScaling" in data:
        import capo_kafkaconnect.types.auto_scaling_update

        out["auto_scaling"] = (
            capo_kafkaconnect.types.auto_scaling_update.deserialize_json(
                data["autoScaling"]
            )
        )
    if "provisionedCapacity" in data:
        import capo_kafkaconnect.types.provisioned_capacity_update

        out["provisioned_capacity"] = (
            capo_kafkaconnect.types.provisioned_capacity_update.deserialize_json(
                data["provisionedCapacity"]
            )
        )
    return out

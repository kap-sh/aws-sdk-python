"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#Capacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.auto_scaling
    import capo_kafkaconnect.types.provisioned_capacity


class Capacity(TypedDict, closed=True):
    auto_scaling: NotRequired["capo_kafkaconnect.types.auto_scaling.AutoScaling"]
    """<p>Information about the auto scaling parameters for the connector.</p>"""
    provisioned_capacity: NotRequired[
        "capo_kafkaconnect.types.provisioned_capacity.ProvisionedCapacity"
    ]
    """<p>Details about a fixed capacity allocated to a connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Capacity) -> dict:
    out: dict = {}
    if "auto_scaling" in value:
        import capo_kafkaconnect.types.auto_scaling

        out["autoScaling"] = capo_kafkaconnect.types.auto_scaling.serialize_json(
            value["auto_scaling"]
        )
    if "provisioned_capacity" in value:
        import capo_kafkaconnect.types.provisioned_capacity

        out["provisionedCapacity"] = (
            capo_kafkaconnect.types.provisioned_capacity.serialize_json(
                value["provisioned_capacity"]
            )
        )
    return out


def deserialize_json(data: dict) -> Capacity:
    out: Capacity = {}  # type: ignore[typeddict-item]
    if "autoScaling" in data:
        import capo_kafkaconnect.types.auto_scaling

        out["auto_scaling"] = capo_kafkaconnect.types.auto_scaling.deserialize_json(
            data["autoScaling"]
        )
    if "provisionedCapacity" in data:
        import capo_kafkaconnect.types.provisioned_capacity

        out["provisioned_capacity"] = (
            capo_kafkaconnect.types.provisioned_capacity.deserialize_json(
                data["provisionedCapacity"]
            )
        )
    return out

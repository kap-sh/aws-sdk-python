"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CapacityDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.auto_scaling_description
    import aws_sdk_kafkaconnect.types.provisioned_capacity_description


class CapacityDescription(TypedDict, closed=True):
    auto_scaling: NotRequired[
        "aws_sdk_kafkaconnect.types.auto_scaling_description.AutoScalingDescription"
    ]
    """<p>Describes the connector's auto scaling capacity.</p>"""
    provisioned_capacity: NotRequired[
        "aws_sdk_kafkaconnect.types.provisioned_capacity_description.ProvisionedCapacityDescription"
    ]
    """<p>Describes a connector's provisioned capacity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityDescription) -> dict:
    out: dict = {}
    if "auto_scaling" in value:
        import aws_sdk_kafkaconnect.types.auto_scaling_description

        out["autoScaling"] = (
            aws_sdk_kafkaconnect.types.auto_scaling_description.serialize_json(
                value["auto_scaling"]
            )
        )
    if "provisioned_capacity" in value:
        import aws_sdk_kafkaconnect.types.provisioned_capacity_description

        out["provisionedCapacity"] = (
            aws_sdk_kafkaconnect.types.provisioned_capacity_description.serialize_json(
                value["provisioned_capacity"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityDescription:
    out: CapacityDescription = {}  # type: ignore[typeddict-item]
    if "autoScaling" in data:
        import aws_sdk_kafkaconnect.types.auto_scaling_description

        out["auto_scaling"] = (
            aws_sdk_kafkaconnect.types.auto_scaling_description.deserialize_json(
                data["autoScaling"]
            )
        )
    if "provisionedCapacity" in data:
        import aws_sdk_kafkaconnect.types.provisioned_capacity_description

        out["provisioned_capacity"] = (
            aws_sdk_kafkaconnect.types.provisioned_capacity_description.deserialize_json(
                data["provisionedCapacity"]
            )
        )
    return out

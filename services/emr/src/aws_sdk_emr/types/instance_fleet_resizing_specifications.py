"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetResizingSpecifications``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.on_demand_resizing_specification
    import aws_sdk_emr.types.spot_resizing_specification


class InstanceFleetResizingSpecifications(TypedDict):
    spot_resize_specification: NotRequired[
        "aws_sdk_emr.types.spot_resizing_specification.SpotResizingSpecification"
    ]
    """<p>The resize specification for Spot Instances in the instance fleet, which contains the allocation strategy and the resize timeout period. </p>"""
    on_demand_resize_specification: NotRequired[
        "aws_sdk_emr.types.on_demand_resizing_specification.OnDemandResizingSpecification"
    ]
    """<p>The resize specification for On-Demand Instances in the instance fleet, which contains the allocation strategy, capacity reservation options, and the resize timeout period. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetResizingSpecifications) -> dict:
    out: dict = {}
    if "spot_resize_specification" in value:
        import aws_sdk_emr.types.spot_resizing_specification

        out["SpotResizeSpecification"] = (
            aws_sdk_emr.types.spot_resizing_specification.serialize_aws_json_1_1(
                value["spot_resize_specification"]
            )
        )
    if "on_demand_resize_specification" in value:
        import aws_sdk_emr.types.on_demand_resizing_specification

        out["OnDemandResizeSpecification"] = (
            aws_sdk_emr.types.on_demand_resizing_specification.serialize_aws_json_1_1(
                value["on_demand_resize_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetResizingSpecifications:
    out: InstanceFleetResizingSpecifications = {}  # type: ignore[typeddict-item]
    if "SpotResizeSpecification" in data:
        import aws_sdk_emr.types.spot_resizing_specification

        out["spot_resize_specification"] = (
            aws_sdk_emr.types.spot_resizing_specification.deserialize_aws_json_1_1(
                data["SpotResizeSpecification"]
            )
        )
    if "OnDemandResizeSpecification" in data:
        import aws_sdk_emr.types.on_demand_resizing_specification

        out["on_demand_resize_specification"] = (
            aws_sdk_emr.types.on_demand_resizing_specification.deserialize_aws_json_1_1(
                data["OnDemandResizeSpecification"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetProvisioningSpecifications``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.on_demand_provisioning_specification
    import capo_emr.types.spot_provisioning_specification


class InstanceFleetProvisioningSpecifications(TypedDict, closed=True):
    spot_specification: NotRequired[
        "capo_emr.types.spot_provisioning_specification.SpotProvisioningSpecification"
    ]
    """<p>The launch specification for Spot instances in the fleet, which determines the allocation strategy, defined duration, and provisioning timeout behavior.</p>"""
    on_demand_specification: NotRequired[
        "capo_emr.types.on_demand_provisioning_specification.OnDemandProvisioningSpecification"
    ]
    """<p> The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy and capacity reservation options.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetProvisioningSpecifications) -> dict:
    out: dict = {}
    if "spot_specification" in value:
        import capo_emr.types.spot_provisioning_specification

        out["SpotSpecification"] = (
            capo_emr.types.spot_provisioning_specification.serialize_aws_json_1_1(
                value["spot_specification"]
            )
        )
    if "on_demand_specification" in value:
        import capo_emr.types.on_demand_provisioning_specification

        out["OnDemandSpecification"] = (
            capo_emr.types.on_demand_provisioning_specification.serialize_aws_json_1_1(
                value["on_demand_specification"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetProvisioningSpecifications:
    out: InstanceFleetProvisioningSpecifications = {}  # type: ignore[typeddict-item]
    if "SpotSpecification" in data:
        import capo_emr.types.spot_provisioning_specification

        out["spot_specification"] = (
            capo_emr.types.spot_provisioning_specification.deserialize_aws_json_1_1(
                data["SpotSpecification"]
            )
        )
    if "OnDemandSpecification" in data:
        import capo_emr.types.on_demand_provisioning_specification

        out["on_demand_specification"] = (
            capo_emr.types.on_demand_provisioning_specification.deserialize_aws_json_1_1(
                data["OnDemandSpecification"]
            )
        )
    return out

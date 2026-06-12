"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#BusinessGoals``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.business_goals_integer


class BusinessGoals(TypedDict):
    speed_of_migration: NotRequired[
        "aws_sdk_migrationhubstrategy.types.business_goals_integer.BusinessGoalsInteger"
    ]
    """<p> Business goal to achieve migration at a fast pace. </p>"""
    reduce_operational_overhead_with_managed_services: NotRequired[
        "aws_sdk_migrationhubstrategy.types.business_goals_integer.BusinessGoalsInteger"
    ]
    """<p> Business goal to reduce the operational overhead on the team by moving into managed services. </p>"""
    modernize_infrastructure_with_cloud_native_technologies: NotRequired[
        "aws_sdk_migrationhubstrategy.types.business_goals_integer.BusinessGoalsInteger"
    ]
    """<p> Business goal to modernize infrastructure by moving to cloud native technologies. </p>"""
    license_cost_reduction: NotRequired[
        "aws_sdk_migrationhubstrategy.types.business_goals_integer.BusinessGoalsInteger"
    ]
    """<p> Business goal to reduce license costs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BusinessGoals) -> dict:
    out: dict = {}
    if "speed_of_migration" in value:
        out["speedOfMigration"] = value["speed_of_migration"]
    if "reduce_operational_overhead_with_managed_services" in value:
        out["reduceOperationalOverheadWithManagedServices"] = value[
            "reduce_operational_overhead_with_managed_services"
        ]
    if "modernize_infrastructure_with_cloud_native_technologies" in value:
        out["modernizeInfrastructureWithCloudNativeTechnologies"] = value[
            "modernize_infrastructure_with_cloud_native_technologies"
        ]
    if "license_cost_reduction" in value:
        out["licenseCostReduction"] = value["license_cost_reduction"]
    return out


def deserialize_json(data: dict) -> BusinessGoals:
    out: BusinessGoals = {}  # type: ignore[typeddict-item]
    if "speedOfMigration" in data:
        out["speed_of_migration"] = data["speedOfMigration"]
    if "reduceOperationalOverheadWithManagedServices" in data:
        out["reduce_operational_overhead_with_managed_services"] = data[
            "reduceOperationalOverheadWithManagedServices"
        ]
    if "modernizeInfrastructureWithCloudNativeTechnologies" in data:
        out["modernize_infrastructure_with_cloud_native_technologies"] = data[
            "modernizeInfrastructureWithCloudNativeTechnologies"
        ]
    if "licenseCostReduction" in data:
        out["license_cost_reduction"] = data["licenseCostReduction"]
    return out

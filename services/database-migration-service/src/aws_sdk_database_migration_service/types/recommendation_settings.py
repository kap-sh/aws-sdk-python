"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RecommendationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class RecommendationSettings(TypedDict):
    instance_sizing_type: "aws_sdk_database_migration_service.types.string.String"
    """<p>The size of your target instance. Fleet Advisor calculates this value based on your data collection type, such as total capacity and resource utilization. Valid values include <code>\"total-capacity\"</code> and <code>\"utilization\"</code>.</p>"""
    workload_type: "aws_sdk_database_migration_service.types.string.String"
    """<p>The deployment option for your target engine. For production databases, Fleet Advisor chooses Multi-AZ deployment. For development or test databases, Fleet Advisor chooses Single-AZ deployment. Valid values include <code>\"development\"</code> and <code>\"production\"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationSettings) -> dict:
    out: dict = {}
    out["InstanceSizingType"] = value["instance_sizing_type"]
    out["WorkloadType"] = value["workload_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationSettings:
    out: RecommendationSettings = {}  # type: ignore[typeddict-item]
    if "InstanceSizingType" in data:
        out["instance_sizing_type"] = data["InstanceSizingType"]
    else:
        raise DeserializationError(
            "RecommendationSettings.instance_sizing_type required"
        )
    if "WorkloadType" in data:
        out["workload_type"] = data["WorkloadType"]
    else:
        raise DeserializationError("RecommendationSettings.workload_type required")
    return out

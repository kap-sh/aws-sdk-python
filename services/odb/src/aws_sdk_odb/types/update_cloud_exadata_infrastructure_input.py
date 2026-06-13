"""Generated from Smithy shape ``com.amazonaws.odb#UpdateCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.maintenance_window
    import aws_sdk_odb.types.resource_id_or_arn


class UpdateCloudExadataInfrastructureInput(TypedDict):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Exadata infrastructure to update.</p>"""
    maintenance_window: NotRequired[
        "aws_sdk_odb.types.maintenance_window.MaintenanceWindow"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCloudExadataInfrastructureInput) -> dict:
    out: dict = {}
    if "maintenance_window" in value:
        import aws_sdk_odb.types.maintenance_window

        out["maintenanceWindow"] = (
            aws_sdk_odb.types.maintenance_window.serialize_aws_json_1_0(
                value["maintenance_window"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCloudExadataInfrastructureInput:
    out: UpdateCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    if "maintenanceWindow" in data:
        import aws_sdk_odb.types.maintenance_window

        out["maintenance_window"] = (
            aws_sdk_odb.types.maintenance_window.deserialize_aws_json_1_0(
                data["maintenanceWindow"]
            )
        )
    return out

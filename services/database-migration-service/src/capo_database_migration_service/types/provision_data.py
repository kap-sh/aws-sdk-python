"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ProvisionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.integer
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class ProvisionData(TypedDict, closed=True):
    provision_state: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The current provisioning state </p>"""
    provisioned_capacity_units: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of capacity units the replication is using.</p>"""
    date_provisioned: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The timestamp when DMS provisioned replication resources.</p>"""
    is_new_provisioning_available: (
        "capo_database_migration_service.types.boolean.Boolean"
    )
    """<p>Whether the new provisioning is available to the replication.</p>"""
    date_new_provisioning_data_available: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The timestamp when provisioning became available.</p>"""
    reason_for_new_provisioning_data: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A message describing the reason that DMS provisioned new resources for the serverless replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionData) -> dict:
    out: dict = {}
    if "provision_state" in value:
        out["ProvisionState"] = value["provision_state"]
    out["ProvisionedCapacityUnits"] = value.get("provisioned_capacity_units", 0)
    if "date_provisioned" in value:
        import capo_database_migration_service.types.t_stamp

        out["DateProvisioned"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["date_provisioned"]
            )
        )
    out["IsNewProvisioningAvailable"] = value.get(
        "is_new_provisioning_available", False
    )
    if "date_new_provisioning_data_available" in value:
        import capo_database_migration_service.types.t_stamp

        out["DateNewProvisioningDataAvailable"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["date_new_provisioning_data_available"]
            )
        )
    if "reason_for_new_provisioning_data" in value:
        out["ReasonForNewProvisioningData"] = value["reason_for_new_provisioning_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionData:
    out: ProvisionData = {}  # type: ignore[typeddict-item]
    if "ProvisionState" in data:
        out["provision_state"] = data["ProvisionState"]
    if "ProvisionedCapacityUnits" in data:
        out["provisioned_capacity_units"] = data["ProvisionedCapacityUnits"]
    else:
        out["provisioned_capacity_units"] = 0
    if "DateProvisioned" in data:
        import capo_database_migration_service.types.t_stamp

        out["date_provisioned"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["DateProvisioned"]
            )
        )
    if "IsNewProvisioningAvailable" in data:
        out["is_new_provisioning_available"] = data["IsNewProvisioningAvailable"]
    else:
        out["is_new_provisioning_available"] = False
    if "DateNewProvisioningDataAvailable" in data:
        import capo_database_migration_service.types.t_stamp

        out["date_new_provisioning_data_available"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["DateNewProvisioningDataAvailable"]
            )
        )
    if "ReasonForNewProvisioningData" in data:
        out["reason_for_new_provisioning_data"] = data["ReasonForNewProvisioningData"]
    return out

"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#UpdateDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_cluster_id
    import aws_sdk_timestream_influxdb.types.db_instance_type
    import aws_sdk_timestream_influxdb.types.db_parameter_group_identifier
    import aws_sdk_timestream_influxdb.types.failover_mode
    import aws_sdk_timestream_influxdb.types.log_delivery_configuration
    import aws_sdk_timestream_influxdb.types.maintenance_schedule
    import aws_sdk_timestream_influxdb.types.port


class UpdateDbClusterInput(TypedDict, closed=True):
    db_cluster_id: "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to update.</p>"""
    log_delivery_configuration: NotRequired[
        "aws_sdk_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>The log delivery configuration to apply to the DB cluster.</p>"""
    db_parameter_group_identifier: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>Update the DB cluster to use the specified DB parameter group.</p>"""
    port: NotRequired["aws_sdk_timestream_influxdb.types.port.Port"]
    """<p>Update the DB cluster to use the specified port.</p>"""
    db_instance_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>Update the DB cluster to use the specified DB instance Type.</p>"""
    failover_mode: NotRequired[
        "aws_sdk_timestream_influxdb.types.failover_mode.FailoverMode"
    ]
    """<p>Update the DB cluster's failover behavior.</p>"""
    maintenance_schedule: NotRequired[
        "aws_sdk_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    if "log_delivery_configuration" in value:
        import aws_sdk_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            aws_sdk_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "port" in value:
        out["port"] = value["port"]
    if "db_instance_type" in value:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "failover_mode" in value:
        import aws_sdk_timestream_influxdb.types.failover_mode

        out["failoverMode"] = (
            aws_sdk_timestream_influxdb.types.failover_mode.serialize_aws_json_1_0(
                value["failover_mode"]
            )
        )
    if "maintenance_schedule" in value:
        import aws_sdk_timestream_influxdb.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            aws_sdk_timestream_influxdb.types.maintenance_schedule.serialize_aws_json_1_0(
                value["maintenance_schedule"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDbClusterInput:
    out: UpdateDbClusterInput = {}  # type: ignore[typeddict-item]
    if "dbClusterId" in data:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        raise DeserializationError("UpdateDbClusterInput.db_cluster_id required")
    if "logDeliveryConfiguration" in data:
        import aws_sdk_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            aws_sdk_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if "dbParameterGroupIdentifier" in data:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if "port" in data:
        out["port"] = data["port"]
    if "dbInstanceType" in data:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if "failoverMode" in data:
        import aws_sdk_timestream_influxdb.types.failover_mode

        out["failover_mode"] = (
            aws_sdk_timestream_influxdb.types.failover_mode.deserialize_aws_json_1_0(
                data["failoverMode"]
            )
        )
    if "maintenanceSchedule" in data:
        import aws_sdk_timestream_influxdb.types.maintenance_schedule

        out["maintenance_schedule"] = (
            aws_sdk_timestream_influxdb.types.maintenance_schedule.deserialize_aws_json_1_0(
                data["maintenanceSchedule"]
            )
        )
    return out

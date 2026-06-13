"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_timestream_influxdb.types.allocated_storage
    import aws_sdk_timestream_influxdb.types.arn
    import aws_sdk_timestream_influxdb.types.cluster_configuration
    import aws_sdk_timestream_influxdb.types.cluster_deployment_type
    import aws_sdk_timestream_influxdb.types.cluster_status
    import aws_sdk_timestream_influxdb.types.db_cluster_id
    import aws_sdk_timestream_influxdb.types.db_cluster_name
    import aws_sdk_timestream_influxdb.types.db_instance_type
    import aws_sdk_timestream_influxdb.types.db_parameter_group_identifier
    import aws_sdk_timestream_influxdb.types.db_storage_type
    import aws_sdk_timestream_influxdb.types.engine_type
    import aws_sdk_timestream_influxdb.types.failover_mode
    import aws_sdk_timestream_influxdb.types.log_delivery_configuration
    import aws_sdk_timestream_influxdb.types.maintenance_schedule
    import aws_sdk_timestream_influxdb.types.network_type
    import aws_sdk_timestream_influxdb.types.port
    import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list
    import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list


class GetDbClusterOutput(TypedDict):
    id: "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to retrieve.</p>"""
    name: "aws_sdk_timestream_influxdb.types.db_cluster_name.DbClusterName"
    """<p>Customer-supplied name of the Timestream for InfluxDB cluster.</p>"""
    arn: "aws_sdk_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB cluster.</p>"""
    status: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_status.ClusterStatus"
    ]
    """<p>The status of the DB cluster.</p>"""
    endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to the Timestream for InfluxDB cluster for write and read operations.</p>"""
    reader_endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to the Timestream for InfluxDB cluster for read-only operations.</p>"""
    port: NotRequired["aws_sdk_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p>"""
    deployment_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
    ]
    """<p>Deployment type of the DB cluster.</p>"""
    db_instance_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB instance type that InfluxDB runs on.</p>"""
    network_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.network_type.NetworkType"
    ]
    """<p>Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_storage_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>"""
    allocated_storage: NotRequired[
        "aws_sdk_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage allocated for your DB storage type (in gibibytes).</p>"""
    engine_type: NotRequired["aws_sdk_timestream_influxdb.types.engine_type.EngineType"]
    """<p>The engine type of your DB cluster.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Indicates if the DB cluster has a public IP to facilitate access from outside the VPC.</p>"""
    db_parameter_group_identifier: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The ID of the DB parameter group assigned to your DB cluster.</p>"""
    log_delivery_configuration: NotRequired[
        "aws_sdk_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to send to specified S3 bucket.</p>"""
    maintenance_schedule: NotRequired[
        "aws_sdk_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The maintenance schedule for the DB cluster.</p>"""
    last_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the last completed maintenance operation on the DB cluster.</p>"""
    next_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the next scheduled maintenance operation on the DB cluster.</p>"""
    influx_auth_parameters_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.</p>"""
    vpc_subnet_ids: NotRequired[
        "aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    ]
    """<p>A list of VPC subnet IDs associated with the DB cluster.</p>"""
    vpc_security_group_ids: NotRequired[
        "aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group IDs associated with the DB cluster.</p>"""
    failover_mode: NotRequired[
        "aws_sdk_timestream_influxdb.types.failover_mode.FailoverMode"
    ]
    """<p>The configured failover mode for the DB cluster.</p>"""
    cluster_configuration: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_configuration.ClusterConfiguration"
    ]
    """<p>Configuration for node modes in the DbCluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbClusterOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["status"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "reader_endpoint" in value:
        out["readerEndpoint"] = value["reader_endpoint"]
    if "port" in value:
        out["port"] = value["port"]
    if "deployment_type" in value:
        import aws_sdk_timestream_influxdb.types.cluster_deployment_type

        out["deploymentType"] = (
            aws_sdk_timestream_influxdb.types.cluster_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "db_instance_type" in value:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
            )
        )
    if "network_type" in value:
        import aws_sdk_timestream_influxdb.types.network_type

        out["networkType"] = (
            aws_sdk_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "db_storage_type" in value:
        import aws_sdk_timestream_influxdb.types.db_storage_type

        out["dbStorageType"] = (
            aws_sdk_timestream_influxdb.types.db_storage_type.serialize_aws_json_1_0(
                value["db_storage_type"]
            )
        )
    if "allocated_storage" in value:
        out["allocatedStorage"] = value["allocated_storage"]
    if "engine_type" in value:
        import aws_sdk_timestream_influxdb.types.engine_type

        out["engineType"] = (
            aws_sdk_timestream_influxdb.types.engine_type.serialize_aws_json_1_0(
                value["engine_type"]
            )
        )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "log_delivery_configuration" in value:
        import aws_sdk_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            aws_sdk_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "maintenance_schedule" in value:
        import aws_sdk_timestream_influxdb.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            aws_sdk_timestream_influxdb.types.maintenance_schedule.serialize_aws_json_1_0(
                value["maintenance_schedule"]
            )
        )
    if "last_maintenance_time" in value:
        import aws_sdk_timestream_influxdb.types._prelude.timestamp

        out["lastMaintenanceTime"] = (
            aws_sdk_timestream_influxdb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_maintenance_time"]
            )
        )
    if "next_maintenance_time" in value:
        import aws_sdk_timestream_influxdb.types._prelude.timestamp

        out["nextMaintenanceTime"] = (
            aws_sdk_timestream_influxdb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["next_maintenance_time"]
            )
        )
    if "influx_auth_parameters_secret_arn" in value:
        out["influxAuthParametersSecretArn"] = value[
            "influx_auth_parameters_secret_arn"
        ]
    if "vpc_subnet_ids" in value:
        import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list

        out["vpcSubnetIds"] = (
            aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.serialize_aws_json_1_0(
                value["vpc_subnet_ids"]
            )
        )
    if "vpc_security_group_ids" in value:
        import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.serialize_aws_json_1_0(
                value["vpc_security_group_ids"]
            )
        )
    if "failover_mode" in value:
        import aws_sdk_timestream_influxdb.types.failover_mode

        out["failoverMode"] = (
            aws_sdk_timestream_influxdb.types.failover_mode.serialize_aws_json_1_0(
                value["failover_mode"]
            )
        )
    if "cluster_configuration" in value:
        import aws_sdk_timestream_influxdb.types.cluster_configuration

        out["clusterConfiguration"] = (
            aws_sdk_timestream_influxdb.types.cluster_configuration.serialize_aws_json_1_0(
                value["cluster_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbClusterOutput:
    out: GetDbClusterOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetDbClusterOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDbClusterOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetDbClusterOutput.arn required")
    if "status" in data:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["status"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "readerEndpoint" in data:
        out["reader_endpoint"] = data["readerEndpoint"]
    if "port" in data:
        out["port"] = data["port"]
    if "deploymentType" in data:
        import aws_sdk_timestream_influxdb.types.cluster_deployment_type

        out["deployment_type"] = (
            aws_sdk_timestream_influxdb.types.cluster_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if "dbInstanceType" in data:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    if "networkType" in data:
        import aws_sdk_timestream_influxdb.types.network_type

        out["network_type"] = (
            aws_sdk_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if "dbStorageType" in data:
        import aws_sdk_timestream_influxdb.types.db_storage_type

        out["db_storage_type"] = (
            aws_sdk_timestream_influxdb.types.db_storage_type.deserialize_aws_json_1_0(
                data["dbStorageType"]
            )
        )
    if "allocatedStorage" in data:
        out["allocated_storage"] = data["allocatedStorage"]
    if "engineType" in data:
        import aws_sdk_timestream_influxdb.types.engine_type

        out["engine_type"] = (
            aws_sdk_timestream_influxdb.types.engine_type.deserialize_aws_json_1_0(
                data["engineType"]
            )
        )
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if "dbParameterGroupIdentifier" in data:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if "logDeliveryConfiguration" in data:
        import aws_sdk_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            aws_sdk_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if "maintenanceSchedule" in data:
        import aws_sdk_timestream_influxdb.types.maintenance_schedule

        out["maintenance_schedule"] = (
            aws_sdk_timestream_influxdb.types.maintenance_schedule.deserialize_aws_json_1_0(
                data["maintenanceSchedule"]
            )
        )
    if "lastMaintenanceTime" in data:
        import aws_sdk_timestream_influxdb.types._prelude.timestamp

        out["last_maintenance_time"] = (
            aws_sdk_timestream_influxdb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastMaintenanceTime"]
            )
        )
    if "nextMaintenanceTime" in data:
        import aws_sdk_timestream_influxdb.types._prelude.timestamp

        out["next_maintenance_time"] = (
            aws_sdk_timestream_influxdb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["nextMaintenanceTime"]
            )
        )
    if "influxAuthParametersSecretArn" in data:
        out["influx_auth_parameters_secret_arn"] = data["influxAuthParametersSecretArn"]
    if "vpcSubnetIds" in data:
        import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list

        out["vpc_subnet_ids"] = (
            aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.deserialize_aws_json_1_0(
                data["vpcSubnetIds"]
            )
        )
    if "vpcSecurityGroupIds" in data:
        import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.deserialize_aws_json_1_0(
                data["vpcSecurityGroupIds"]
            )
        )
    if "failoverMode" in data:
        import aws_sdk_timestream_influxdb.types.failover_mode

        out["failover_mode"] = (
            aws_sdk_timestream_influxdb.types.failover_mode.deserialize_aws_json_1_0(
                data["failoverMode"]
            )
        )
    if "clusterConfiguration" in data:
        import aws_sdk_timestream_influxdb.types.cluster_configuration

        out["cluster_configuration"] = (
            aws_sdk_timestream_influxdb.types.cluster_configuration.deserialize_aws_json_1_0(
                data["clusterConfiguration"]
            )
        )
    return out

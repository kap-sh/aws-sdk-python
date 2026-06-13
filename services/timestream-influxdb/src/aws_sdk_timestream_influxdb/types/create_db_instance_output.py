"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbInstanceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_timestream_influxdb.types.allocated_storage
    import aws_sdk_timestream_influxdb.types.arn
    import aws_sdk_timestream_influxdb.types.db_cluster_id
    import aws_sdk_timestream_influxdb.types.db_instance_id
    import aws_sdk_timestream_influxdb.types.db_instance_name
    import aws_sdk_timestream_influxdb.types.db_instance_type
    import aws_sdk_timestream_influxdb.types.db_parameter_group_identifier
    import aws_sdk_timestream_influxdb.types.db_storage_type
    import aws_sdk_timestream_influxdb.types.deployment_type
    import aws_sdk_timestream_influxdb.types.instance_mode
    import aws_sdk_timestream_influxdb.types.instance_mode_list
    import aws_sdk_timestream_influxdb.types.log_delivery_configuration
    import aws_sdk_timestream_influxdb.types.maintenance_schedule
    import aws_sdk_timestream_influxdb.types.network_type
    import aws_sdk_timestream_influxdb.types.port
    import aws_sdk_timestream_influxdb.types.status
    import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list
    import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list


class CreateDbInstanceOutput(TypedDict):
    id: "aws_sdk_timestream_influxdb.types.db_instance_id.DbInstanceId"
    """<p>A service-generated unique identifier.</p>"""
    name: "aws_sdk_timestream_influxdb.types.db_instance_name.DbInstanceName"
    """<p>The customer-supplied name that uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands.</p>"""
    arn: "aws_sdk_timestream_influxdb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the DB instance.</p>"""
    status: NotRequired["aws_sdk_timestream_influxdb.types.status.Status"]
    """<p>The status of the DB instance.</p>"""
    endpoint: NotRequired["str"]
    """<p>The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.</p>"""
    port: NotRequired["aws_sdk_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections. The default value is 8086.</p>"""
    network_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.network_type.NetworkType"
    ]
    """<p>Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    db_instance_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_instance_type.DbInstanceType"
    ]
    """<p>The Timestream for InfluxDB instance type that InfluxDB runs on.</p>"""
    db_storage_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type that InfluxDB stores data on.</p>"""
    allocated_storage: NotRequired[
        "aws_sdk_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage allocated for your DB storage type (in gibibytes).</p>"""
    deployment_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.deployment_type.DeploymentType"
    ]
    """<p>Specifies whether the Timestream for InfluxDB is deployed as Single-AZ or with a MultiAZ Standby for High availability.</p>"""
    vpc_subnet_ids: (
        "aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    )
    """<p>A list of VPC subnet IDs associated with the DB instance.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Indicates if the DB instance has a public IP to facilitate access.</p>"""
    vpc_security_group_ids: NotRequired[
        "aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of VPC security group IDs associated with the DB instance.</p>"""
    db_parameter_group_identifier: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The id of the DB parameter group assigned to your DB instance.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone in which the DB instance resides.</p>"""
    secondary_availability_zone: NotRequired["str"]
    """<p>The Availability Zone in which the standby instance is located when deploying with a MultiAZ standby instance.</p>"""
    log_delivery_configuration: NotRequired[
        "aws_sdk_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to send to specified S3 bucket.</p>"""
    influx_auth_parameters_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.</p>"""
    db_cluster_id: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    ]
    """<p>Specifies the DbCluster to which this DbInstance belongs to.</p>"""
    instance_mode: NotRequired[
        "aws_sdk_timestream_influxdb.types.instance_mode.InstanceMode"
    ]
    """<p>Specifies the DbInstance's role in the cluster.</p>"""
    instance_modes: NotRequired[
        "aws_sdk_timestream_influxdb.types.instance_mode_list.InstanceModeList"
    ]
    """<p>Specifies the DbInstance's roles in the cluster.</p>"""
    maintenance_schedule: NotRequired[
        "aws_sdk_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The maintenance schedule for the DB instance.</p>"""
    last_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the last completed maintenance operation on the DB instance.</p>"""
    next_maintenance_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of the next scheduled maintenance operation on the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbInstanceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_timestream_influxdb.types.status

        out["status"] = aws_sdk_timestream_influxdb.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "port" in value:
        out["port"] = value["port"]
    if "network_type" in value:
        import aws_sdk_timestream_influxdb.types.network_type

        out["networkType"] = (
            aws_sdk_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "db_instance_type" in value:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["dbInstanceType"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.serialize_aws_json_1_0(
                value["db_instance_type"]
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
    if "deployment_type" in value:
        import aws_sdk_timestream_influxdb.types.deployment_type

        out["deploymentType"] = (
            aws_sdk_timestream_influxdb.types.deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list

    out["vpcSubnetIds"] = (
        aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.serialize_aws_json_1_0(
            value["vpc_subnet_ids"]
        )
    )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "vpc_security_group_ids" in value:
        import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list

        out["vpcSecurityGroupIds"] = (
            aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.serialize_aws_json_1_0(
                value["vpc_security_group_ids"]
            )
        )
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "secondary_availability_zone" in value:
        out["secondaryAvailabilityZone"] = value["secondary_availability_zone"]
    if "log_delivery_configuration" in value:
        import aws_sdk_timestream_influxdb.types.log_delivery_configuration

        out["logDeliveryConfiguration"] = (
            aws_sdk_timestream_influxdb.types.log_delivery_configuration.serialize_aws_json_1_0(
                value["log_delivery_configuration"]
            )
        )
    if "influx_auth_parameters_secret_arn" in value:
        out["influxAuthParametersSecretArn"] = value[
            "influx_auth_parameters_secret_arn"
        ]
    if "db_cluster_id" in value:
        out["dbClusterId"] = value["db_cluster_id"]
    if "instance_mode" in value:
        import aws_sdk_timestream_influxdb.types.instance_mode

        out["instanceMode"] = (
            aws_sdk_timestream_influxdb.types.instance_mode.serialize_aws_json_1_0(
                value["instance_mode"]
            )
        )
    if "instance_modes" in value:
        import aws_sdk_timestream_influxdb.types.instance_mode_list

        out["instanceModes"] = (
            aws_sdk_timestream_influxdb.types.instance_mode_list.serialize_aws_json_1_0(
                value["instance_modes"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbInstanceOutput:
    out: CreateDbInstanceOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateDbInstanceOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDbInstanceOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateDbInstanceOutput.arn required")
    if "status" in data:
        import aws_sdk_timestream_influxdb.types.status

        out["status"] = (
            aws_sdk_timestream_influxdb.types.status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "port" in data:
        out["port"] = data["port"]
    if "networkType" in data:
        import aws_sdk_timestream_influxdb.types.network_type

        out["network_type"] = (
            aws_sdk_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if "dbInstanceType" in data:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
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
    if "deploymentType" in data:
        import aws_sdk_timestream_influxdb.types.deployment_type

        out["deployment_type"] = (
            aws_sdk_timestream_influxdb.types.deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if "vpcSubnetIds" in data:
        import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list

        out["vpc_subnet_ids"] = (
            aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.deserialize_aws_json_1_0(
                data["vpcSubnetIds"]
            )
        )
    else:
        raise DeserializationError("CreateDbInstanceOutput.vpc_subnet_ids required")
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if "vpcSecurityGroupIds" in data:
        import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.deserialize_aws_json_1_0(
                data["vpcSecurityGroupIds"]
            )
        )
    if "dbParameterGroupIdentifier" in data:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "secondaryAvailabilityZone" in data:
        out["secondary_availability_zone"] = data["secondaryAvailabilityZone"]
    if "logDeliveryConfiguration" in data:
        import aws_sdk_timestream_influxdb.types.log_delivery_configuration

        out["log_delivery_configuration"] = (
            aws_sdk_timestream_influxdb.types.log_delivery_configuration.deserialize_aws_json_1_0(
                data["logDeliveryConfiguration"]
            )
        )
    if "influxAuthParametersSecretArn" in data:
        out["influx_auth_parameters_secret_arn"] = data["influxAuthParametersSecretArn"]
    if "dbClusterId" in data:
        out["db_cluster_id"] = data["dbClusterId"]
    if "instanceMode" in data:
        import aws_sdk_timestream_influxdb.types.instance_mode

        out["instance_mode"] = (
            aws_sdk_timestream_influxdb.types.instance_mode.deserialize_aws_json_1_0(
                data["instanceMode"]
            )
        )
    if "instanceModes" in data:
        import aws_sdk_timestream_influxdb.types.instance_mode_list

        out["instance_modes"] = (
            aws_sdk_timestream_influxdb.types.instance_mode_list.deserialize_aws_json_1_0(
                data["instanceModes"]
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
    return out

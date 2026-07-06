"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.allocated_storage
    import aws_sdk_timestream_influxdb.types.bucket
    import aws_sdk_timestream_influxdb.types.cluster_deployment_type
    import aws_sdk_timestream_influxdb.types.db_cluster_name
    import aws_sdk_timestream_influxdb.types.db_instance_type
    import aws_sdk_timestream_influxdb.types.db_parameter_group_identifier
    import aws_sdk_timestream_influxdb.types.db_storage_type
    import aws_sdk_timestream_influxdb.types.failover_mode
    import aws_sdk_timestream_influxdb.types.log_delivery_configuration
    import aws_sdk_timestream_influxdb.types.maintenance_schedule
    import aws_sdk_timestream_influxdb.types.network_type
    import aws_sdk_timestream_influxdb.types.organization
    import aws_sdk_timestream_influxdb.types.password
    import aws_sdk_timestream_influxdb.types.port
    import aws_sdk_timestream_influxdb.types.request_tag_map
    import aws_sdk_timestream_influxdb.types.username
    import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list
    import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list


class CreateDbClusterInput(TypedDict, closed=True):
    name: "aws_sdk_timestream_influxdb.types.db_cluster_name.DbClusterName"
    """<p>The name that uniquely identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and CLI commands. This name will also be a prefix included in the endpoint. DB cluster names must be unique per customer and per region.</p>"""
    username: NotRequired["aws_sdk_timestream_influxdb.types.username.Username"]
    """<p>The username of the initial admin user created in InfluxDB. Must start with a letter and can't end with a hyphen or contain two consecutive hyphens. For example, my-user1. This username will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>"""
    password: NotRequired["aws_sdk_timestream_influxdb.types.password.Password"]
    """<p>The password of the initial admin user created in InfluxDB. This password will allow you to access the InfluxDB UI to perform various administrative tasks and also use the InfluxDB CLI to create an operator token. These attributes will be stored in a secret created in Secrets Manager in your account.</p>"""
    organization: NotRequired[
        "aws_sdk_timestream_influxdb.types.organization.Organization"
    ]
    """<p>The name of the initial organization for the initial admin user in InfluxDB. An InfluxDB organization is a workspace for a group of users.</p>"""
    bucket: NotRequired["aws_sdk_timestream_influxdb.types.bucket.Bucket"]
    """<p>The name of the initial InfluxDB bucket. All InfluxDB data is stored in a bucket. A bucket combines the concept of a database and a retention period (the duration of time that each data point persists). A bucket belongs to an organization.</p>"""
    port: NotRequired["aws_sdk_timestream_influxdb.types.port.Port"]
    """<p>The port number on which InfluxDB accepts connections.</p> <p>Valid Values: 1024-65535</p> <p>Default: 8086 for InfluxDB v2, 8181 for InfluxDB v3</p> <p>Constraints: The value can't be 2375-2376, 7788-7799, 8090, or 51678-51680</p>"""
    db_parameter_group_identifier: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_parameter_group_identifier.DbParameterGroupIdentifier"
    ]
    """<p>The ID of the DB parameter group to assign to your DB cluster. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.</p>"""
    db_instance_type: (
        "aws_sdk_timestream_influxdb.types.db_instance_type.DbInstanceType"
    )
    """<p>The Timestream for InfluxDB DB instance type to run InfluxDB on.</p>"""
    db_storage_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_storage_type.DbStorageType"
    ]
    """<p>The Timestream for InfluxDB DB storage type to read and write InfluxDB data.</p> <p>You can choose between three different types of provisioned Influx IOPS Included storage according to your workload requirements:</p> <ul> <li> <p>Influx I/O Included 3000 IOPS</p> </li> <li> <p>Influx I/O Included 12000 IOPS</p> </li> <li> <p>Influx I/O Included 16000 IOPS</p> </li> </ul>"""
    allocated_storage: NotRequired[
        "aws_sdk_timestream_influxdb.types.allocated_storage.AllocatedStorage"
    ]
    """<p>The amount of storage to allocate for your DB storage type in GiB (gibibytes).</p>"""
    network_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.network_type.NetworkType"
    ]
    """<p>Specifies whether the network type of the Timestream for InfluxDB cluster is IPv4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>Configures the Timestream for InfluxDB cluster with a public IP to facilitate access from outside the VPC.</p>"""
    vpc_subnet_ids: (
        "aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.VpcSubnetIdList"
    )
    """<p>A list of VPC subnet IDs to associate with the DB cluster. Provide at least two VPC subnet IDs in different Availability Zones when deploying with a Multi-AZ standby.</p>"""
    vpc_security_group_ids: "aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    """<p>A list of VPC security group IDs to associate with the Timestream for InfluxDB cluster.</p>"""
    deployment_type: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_deployment_type.ClusterDeploymentType"
    ]
    """<p>Specifies the type of cluster to create.</p>"""
    failover_mode: NotRequired[
        "aws_sdk_timestream_influxdb.types.failover_mode.FailoverMode"
    ]
    """<p>Specifies the behavior of failure recovery when the primary node of the cluster fails.</p>"""
    log_delivery_configuration: NotRequired[
        "aws_sdk_timestream_influxdb.types.log_delivery_configuration.LogDeliveryConfiguration"
    ]
    """<p>Configuration for sending InfluxDB engine logs to a specified S3 bucket.</p>"""
    maintenance_schedule: NotRequired[
        "aws_sdk_timestream_influxdb.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>Specifies the maintenance schedule for the DB cluster, including the preferred maintenance window and timezone.</p>"""
    tags: NotRequired["aws_sdk_timestream_influxdb.types.request_tag_map.RequestTagMap"]
    """<p>A list of key-value pairs to associate with the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbClusterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "username" in value:
        out["username"] = value["username"]
    if "password" in value:
        out["password"] = value["password"]
    if "organization" in value:
        out["organization"] = value["organization"]
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "port" in value:
        out["port"] = value["port"]
    if "db_parameter_group_identifier" in value:
        out["dbParameterGroupIdentifier"] = value["db_parameter_group_identifier"]
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
    if "network_type" in value:
        import aws_sdk_timestream_influxdb.types.network_type

        out["networkType"] = (
            aws_sdk_timestream_influxdb.types.network_type.serialize_aws_json_1_0(
                value["network_type"]
            )
        )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list

    out["vpcSubnetIds"] = (
        aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.serialize_aws_json_1_0(
            value["vpc_subnet_ids"]
        )
    )
    import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list

    out["vpcSecurityGroupIds"] = (
        aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.serialize_aws_json_1_0(
            value["vpc_security_group_ids"]
        )
    )
    if "deployment_type" in value:
        import aws_sdk_timestream_influxdb.types.cluster_deployment_type

        out["deploymentType"] = (
            aws_sdk_timestream_influxdb.types.cluster_deployment_type.serialize_aws_json_1_0(
                value["deployment_type"]
            )
        )
    if "failover_mode" in value:
        import aws_sdk_timestream_influxdb.types.failover_mode

        out["failoverMode"] = (
            aws_sdk_timestream_influxdb.types.failover_mode.serialize_aws_json_1_0(
                value["failover_mode"]
            )
        )
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
    if "tags" in value:
        import aws_sdk_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            aws_sdk_timestream_influxdb.types.request_tag_map.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbClusterInput:
    out: CreateDbClusterInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDbClusterInput.name required")
    if "username" in data:
        out["username"] = data["username"]
    if "password" in data:
        out["password"] = data["password"]
    if "organization" in data:
        out["organization"] = data["organization"]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "port" in data:
        out["port"] = data["port"]
    if "dbParameterGroupIdentifier" in data:
        out["db_parameter_group_identifier"] = data["dbParameterGroupIdentifier"]
    if "dbInstanceType" in data:
        import aws_sdk_timestream_influxdb.types.db_instance_type

        out["db_instance_type"] = (
            aws_sdk_timestream_influxdb.types.db_instance_type.deserialize_aws_json_1_0(
                data["dbInstanceType"]
            )
        )
    else:
        raise DeserializationError("CreateDbClusterInput.db_instance_type required")
    if "dbStorageType" in data:
        import aws_sdk_timestream_influxdb.types.db_storage_type

        out["db_storage_type"] = (
            aws_sdk_timestream_influxdb.types.db_storage_type.deserialize_aws_json_1_0(
                data["dbStorageType"]
            )
        )
    if "allocatedStorage" in data:
        out["allocated_storage"] = data["allocatedStorage"]
    if "networkType" in data:
        import aws_sdk_timestream_influxdb.types.network_type

        out["network_type"] = (
            aws_sdk_timestream_influxdb.types.network_type.deserialize_aws_json_1_0(
                data["networkType"]
            )
        )
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if "vpcSubnetIds" in data:
        import aws_sdk_timestream_influxdb.types.vpc_subnet_id_list

        out["vpc_subnet_ids"] = (
            aws_sdk_timestream_influxdb.types.vpc_subnet_id_list.deserialize_aws_json_1_0(
                data["vpcSubnetIds"]
            )
        )
    else:
        raise DeserializationError("CreateDbClusterInput.vpc_subnet_ids required")
    if "vpcSecurityGroupIds" in data:
        import aws_sdk_timestream_influxdb.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            aws_sdk_timestream_influxdb.types.vpc_security_group_id_list.deserialize_aws_json_1_0(
                data["vpcSecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDbClusterInput.vpc_security_group_ids required"
        )
    if "deploymentType" in data:
        import aws_sdk_timestream_influxdb.types.cluster_deployment_type

        out["deployment_type"] = (
            aws_sdk_timestream_influxdb.types.cluster_deployment_type.deserialize_aws_json_1_0(
                data["deploymentType"]
            )
        )
    if "failoverMode" in data:
        import aws_sdk_timestream_influxdb.types.failover_mode

        out["failover_mode"] = (
            aws_sdk_timestream_influxdb.types.failover_mode.deserialize_aws_json_1_0(
                data["failoverMode"]
            )
        )
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
    if "tags" in data:
        import aws_sdk_timestream_influxdb.types.request_tag_map

        out["tags"] = (
            aws_sdk_timestream_influxdb.types.request_tag_map.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out

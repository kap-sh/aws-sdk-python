"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.auto_scaling_configuration
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.capacity_configuration
    import aws_sdk_finspace.types.client_token
    import aws_sdk_finspace.types.code_configuration
    import aws_sdk_finspace.types.execution_role_arn
    import aws_sdk_finspace.types.initialization_script_file_path
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_cache_storage_configurations
    import aws_sdk_finspace.types.kx_cluster_description
    import aws_sdk_finspace.types.kx_cluster_name
    import aws_sdk_finspace.types.kx_cluster_type
    import aws_sdk_finspace.types.kx_command_line_arguments
    import aws_sdk_finspace.types.kx_database_configurations
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_savedown_storage_configuration
    import aws_sdk_finspace.types.kx_scaling_group_configuration
    import aws_sdk_finspace.types.release_label
    import aws_sdk_finspace.types.tag_map
    import aws_sdk_finspace.types.tickerplant_log_configuration
    import aws_sdk_finspace.types.vpc_configuration


class CreateKxClusterRequest(TypedDict):
    client_token: NotRequired["aws_sdk_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    cluster_name: "aws_sdk_finspace.types.kx_cluster_name.KxClusterName"
    """<p>A unique name for the cluster that you want to create.</p>"""
    cluster_type: "aws_sdk_finspace.types.kx_cluster_type.KxClusterType"
    """<p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>"""
    tickerplant_log_configuration: NotRequired[
        "aws_sdk_finspace.types.tickerplant_log_configuration.TickerplantLogConfiguration"
    ]
    """<p> A configuration to store Tickerplant logs. It consists of a list of volumes that will be mounted to your cluster. For the cluster type <code>Tickerplant</code>, the location of the TP volume on the cluster will be available by using the global variable <code>.aws.tp_log_path</code>. </p>"""
    databases: NotRequired[
        "aws_sdk_finspace.types.kx_database_configurations.KxDatabaseConfigurations"
    ]
    """<p>A list of databases that will be available for querying.</p>"""
    cache_storage_configurations: NotRequired[
        "aws_sdk_finspace.types.kx_cache_storage_configurations.KxCacheStorageConfigurations"
    ]
    """<p>The configurations for a read only cache storage associated with a cluster. This cache will be stored as an FSx Lustre that reads from the S3 store. </p>"""
    auto_scaling_configuration: NotRequired[
        "aws_sdk_finspace.types.auto_scaling_configuration.AutoScalingConfiguration"
    ]
    """<p>The configuration based on which FinSpace will scale in or scale out nodes in your cluster.</p>"""
    cluster_description: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_description.KxClusterDescription"
    ]
    """<p>A description of the cluster.</p>"""
    capacity_configuration: NotRequired[
        "aws_sdk_finspace.types.capacity_configuration.CapacityConfiguration"
    ]
    """<p>A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.</p>"""
    release_label: "aws_sdk_finspace.types.release_label.ReleaseLabel"
    """<p>The version of FinSpace managed kdb to run.</p>"""
    vpc_configuration: "aws_sdk_finspace.types.vpc_configuration.VpcConfiguration"
    """<p>Configuration details about the network where the Privatelink endpoint of the cluster resides.</p>"""
    initialization_script: NotRequired[
        "aws_sdk_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
    ]
    """<p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p>"""
    command_line_arguments: NotRequired[
        "aws_sdk_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
    ]
    """<p>Defines the key-value pairs to make them available inside the cluster.</p>"""
    code: NotRequired["aws_sdk_finspace.types.code_configuration.CodeConfiguration"]
    """<p>The details of the custom code that you want to use inside a cluster when analyzing a data. It consists of the S3 source bucket, location, S3 object version, and the relative path from where the custom code is loaded into the cluster. </p>"""
    execution_role: NotRequired[
        "aws_sdk_finspace.types.execution_role_arn.ExecutionRoleArn"
    ]
    """<p>An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.</p>"""
    savedown_storage_configuration: NotRequired[
        "aws_sdk_finspace.types.kx_savedown_storage_configuration.KxSavedownStorageConfiguration"
    ]
    """<p>The size and type of the temporary storage that is used to hold data during the savedown process. This parameter is required when you choose <code>clusterType</code> as RDB. All the data written to this storage space is lost when the cluster node is restarted.</p>"""
    az_mode: "aws_sdk_finspace.types.kx_az_mode.KxAzMode"
    """<p>The number of availability zones you want to assign per cluster. This can be one of the following </p> <ul> <li> <p> <code>SINGLE</code> – Assigns one availability zone per cluster.</p> </li> <li> <p> <code>MULTI</code> – Assigns all the availability zones per cluster.</p> </li> </ul>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The availability zone identifiers for the requested regions.</p>"""
    tags: NotRequired["aws_sdk_finspace.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to label the cluster. You can add up to 50 tags to a cluster.</p>"""
    scaling_group_configuration: NotRequired[
        "aws_sdk_finspace.types.kx_scaling_group_configuration.KxScalingGroupConfiguration"
    ]
    """<p>The structure that stores the configuration details of a scaling group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxClusterRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["clusterName"] = value["cluster_name"]
    import aws_sdk_finspace.types.kx_cluster_type

    out["clusterType"] = aws_sdk_finspace.types.kx_cluster_type.serialize_json(
        value["cluster_type"]
    )
    if "tickerplant_log_configuration" in value:
        import aws_sdk_finspace.types.tickerplant_log_configuration

        out["tickerplantLogConfiguration"] = (
            aws_sdk_finspace.types.tickerplant_log_configuration.serialize_json(
                value["tickerplant_log_configuration"]
            )
        )
    if "databases" in value:
        import aws_sdk_finspace.types.kx_database_configurations

        out["databases"] = (
            aws_sdk_finspace.types.kx_database_configurations.serialize_json(
                value["databases"]
            )
        )
    if "cache_storage_configurations" in value:
        import aws_sdk_finspace.types.kx_cache_storage_configurations

        out["cacheStorageConfigurations"] = (
            aws_sdk_finspace.types.kx_cache_storage_configurations.serialize_json(
                value["cache_storage_configurations"]
            )
        )
    if "auto_scaling_configuration" in value:
        import aws_sdk_finspace.types.auto_scaling_configuration

        out["autoScalingConfiguration"] = (
            aws_sdk_finspace.types.auto_scaling_configuration.serialize_json(
                value["auto_scaling_configuration"]
            )
        )
    if "cluster_description" in value:
        out["clusterDescription"] = value["cluster_description"]
    if "capacity_configuration" in value:
        import aws_sdk_finspace.types.capacity_configuration

        out["capacityConfiguration"] = (
            aws_sdk_finspace.types.capacity_configuration.serialize_json(
                value["capacity_configuration"]
            )
        )
    out["releaseLabel"] = value["release_label"]
    import aws_sdk_finspace.types.vpc_configuration

    out["vpcConfiguration"] = aws_sdk_finspace.types.vpc_configuration.serialize_json(
        value["vpc_configuration"]
    )
    if "initialization_script" in value:
        out["initializationScript"] = value["initialization_script"]
    if "command_line_arguments" in value:
        import aws_sdk_finspace.types.kx_command_line_arguments

        out["commandLineArguments"] = (
            aws_sdk_finspace.types.kx_command_line_arguments.serialize_json(
                value["command_line_arguments"]
            )
        )
    if "code" in value:
        import aws_sdk_finspace.types.code_configuration

        out["code"] = aws_sdk_finspace.types.code_configuration.serialize_json(
            value["code"]
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "savedown_storage_configuration" in value:
        import aws_sdk_finspace.types.kx_savedown_storage_configuration

        out["savedownStorageConfiguration"] = (
            aws_sdk_finspace.types.kx_savedown_storage_configuration.serialize_json(
                value["savedown_storage_configuration"]
            )
        )
    import aws_sdk_finspace.types.kx_az_mode

    out["azMode"] = aws_sdk_finspace.types.kx_az_mode.serialize_json(value["az_mode"])
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "tags" in value:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.serialize_json(value["tags"])
    if "scaling_group_configuration" in value:
        import aws_sdk_finspace.types.kx_scaling_group_configuration

        out["scalingGroupConfiguration"] = (
            aws_sdk_finspace.types.kx_scaling_group_configuration.serialize_json(
                value["scaling_group_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateKxClusterRequest:
    out: CreateKxClusterRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("CreateKxClusterRequest.cluster_name required")
    if "clusterType" in data:
        import aws_sdk_finspace.types.kx_cluster_type

        out["cluster_type"] = aws_sdk_finspace.types.kx_cluster_type.deserialize_json(
            data["clusterType"]
        )
    else:
        raise DeserializationError("CreateKxClusterRequest.cluster_type required")
    if "tickerplantLogConfiguration" in data:
        import aws_sdk_finspace.types.tickerplant_log_configuration

        out["tickerplant_log_configuration"] = (
            aws_sdk_finspace.types.tickerplant_log_configuration.deserialize_json(
                data["tickerplantLogConfiguration"]
            )
        )
    if "databases" in data:
        import aws_sdk_finspace.types.kx_database_configurations

        out["databases"] = (
            aws_sdk_finspace.types.kx_database_configurations.deserialize_json(
                data["databases"]
            )
        )
    if "cacheStorageConfigurations" in data:
        import aws_sdk_finspace.types.kx_cache_storage_configurations

        out["cache_storage_configurations"] = (
            aws_sdk_finspace.types.kx_cache_storage_configurations.deserialize_json(
                data["cacheStorageConfigurations"]
            )
        )
    if "autoScalingConfiguration" in data:
        import aws_sdk_finspace.types.auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            aws_sdk_finspace.types.auto_scaling_configuration.deserialize_json(
                data["autoScalingConfiguration"]
            )
        )
    if "clusterDescription" in data:
        out["cluster_description"] = data["clusterDescription"]
    if "capacityConfiguration" in data:
        import aws_sdk_finspace.types.capacity_configuration

        out["capacity_configuration"] = (
            aws_sdk_finspace.types.capacity_configuration.deserialize_json(
                data["capacityConfiguration"]
            )
        )
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("CreateKxClusterRequest.release_label required")
    if "vpcConfiguration" in data:
        import aws_sdk_finspace.types.vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_finspace.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateKxClusterRequest.vpc_configuration required")
    if "initializationScript" in data:
        out["initialization_script"] = data["initializationScript"]
    if "commandLineArguments" in data:
        import aws_sdk_finspace.types.kx_command_line_arguments

        out["command_line_arguments"] = (
            aws_sdk_finspace.types.kx_command_line_arguments.deserialize_json(
                data["commandLineArguments"]
            )
        )
    if "code" in data:
        import aws_sdk_finspace.types.code_configuration

        out["code"] = aws_sdk_finspace.types.code_configuration.deserialize_json(
            data["code"]
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "savedownStorageConfiguration" in data:
        import aws_sdk_finspace.types.kx_savedown_storage_configuration

        out["savedown_storage_configuration"] = (
            aws_sdk_finspace.types.kx_savedown_storage_configuration.deserialize_json(
                data["savedownStorageConfiguration"]
            )
        )
    if "azMode" in data:
        import aws_sdk_finspace.types.kx_az_mode

        out["az_mode"] = aws_sdk_finspace.types.kx_az_mode.deserialize_json(
            data["azMode"]
        )
    else:
        raise DeserializationError("CreateKxClusterRequest.az_mode required")
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "tags" in data:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.deserialize_json(data["tags"])
    if "scalingGroupConfiguration" in data:
        import aws_sdk_finspace.types.kx_scaling_group_configuration

        out["scaling_group_configuration"] = (
            aws_sdk_finspace.types.kx_scaling_group_configuration.deserialize_json(
                data["scalingGroupConfiguration"]
            )
        )
    return out

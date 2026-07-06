"""Generated from Smithy shape ``com.amazonaws.emrserverless#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_arn
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.application_name
    import aws_sdk_emr_serverless.types.application_state
    import aws_sdk_emr_serverless.types.architecture
    import aws_sdk_emr_serverless.types.auto_start_config
    import aws_sdk_emr_serverless.types.auto_stop_config
    import aws_sdk_emr_serverless.types.configuration_list
    import aws_sdk_emr_serverless.types.date
    import aws_sdk_emr_serverless.types.disk_encryption_configuration
    import aws_sdk_emr_serverless.types.engine_type
    import aws_sdk_emr_serverless.types.identity_center_configuration
    import aws_sdk_emr_serverless.types.image_configuration
    import aws_sdk_emr_serverless.types.initial_capacity_config_map
    import aws_sdk_emr_serverless.types.interactive_configuration
    import aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration
    import aws_sdk_emr_serverless.types.maximum_allowed_resources
    import aws_sdk_emr_serverless.types.monitoring_configuration
    import aws_sdk_emr_serverless.types.network_configuration
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.scheduler_configuration
    import aws_sdk_emr_serverless.types.string256
    import aws_sdk_emr_serverless.types.tag_map
    import aws_sdk_emr_serverless.types.worker_type_specification_map


class Application(TypedDict, closed=True):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    name: NotRequired["aws_sdk_emr_serverless.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    arn: "aws_sdk_emr_serverless.types.application_arn.ApplicationArn"
    """<p>The ARN of the application.</p>"""
    release_label: "aws_sdk_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release associated with the application.</p>"""
    type: "aws_sdk_emr_serverless.types.engine_type.EngineType"
    """<p>The type of application, such as Spark or Hive.</p>"""
    state: "aws_sdk_emr_serverless.types.application_state.ApplicationState"
    """<p>The state of the application.</p>"""
    state_details: NotRequired["aws_sdk_emr_serverless.types.string256.String256"]
    """<p>The state details of the application.</p>"""
    initial_capacity: NotRequired[
        "aws_sdk_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
    ]
    """<p>The initial capacity of the application.</p>"""
    maximum_capacity: NotRequired[
        "aws_sdk_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
    ]
    """<p>The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.</p>"""
    created_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the application run was created.</p>"""
    updated_at: "aws_sdk_emr_serverless.types.date.Date"
    """<p>The date and time when the application run was last updated.</p>"""
    tags: NotRequired["aws_sdk_emr_serverless.types.tag_map.TagMap"]
    """<p>The tags assigned to the application.</p>"""
    auto_start_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.auto_start_config.AutoStartConfig"
    ]
    """<p>The configuration for an application to automatically start on job submission.</p>"""
    auto_stop_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.auto_stop_config.AutoStopConfig"
    ]
    """<p>The configuration for an application to automatically stop after a certain amount of time being idle.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for customer VPC connectivity for the application.</p>"""
    architecture: NotRequired["aws_sdk_emr_serverless.types.architecture.Architecture"]
    """<p>The CPU architecture of an application.</p>"""
    image_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.image_configuration.ImageConfiguration"
    ]
    """<p>The image configuration applied to all worker types.</p>"""
    worker_type_specifications: NotRequired[
        "aws_sdk_emr_serverless.types.worker_type_specification_map.WorkerTypeSpecificationMap"
    ]
    """<p>The specification applied to each worker type.</p>"""
    runtime_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.configuration_list.ConfigurationList"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html\">Configuration</a> specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the <a href=\"https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html\">GetApplication</a> API operation.</p>"""
    monitoring_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
    ]
    disk_encryption_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
    ]
    """<p>The configuration object that allows encrypting local disks.</p>"""
    interactive_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
    ]
    """<p>The interactive configuration object that enables the interactive use cases for an application.</p>"""
    scheduler_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
    ]
    """<p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>"""
    identity_center_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.identity_center_configuration.IdentityCenterConfiguration"
    ]
    """<p>The IAM Identity Center configuration applied to enable trusted identity propagation.</p>"""
    job_level_cost_allocation_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
    ]
    """<p>The configuration object that enables job level cost allocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["releaseLabel"] = value["release_label"]
    out["type"] = value["type"]
    out["state"] = value["state"]
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "initial_capacity" in value:
        import aws_sdk_emr_serverless.types.initial_capacity_config_map

        out["initialCapacity"] = (
            aws_sdk_emr_serverless.types.initial_capacity_config_map.serialize_json(
                value["initial_capacity"]
            )
        )
    if "maximum_capacity" in value:
        import aws_sdk_emr_serverless.types.maximum_allowed_resources

        out["maximumCapacity"] = (
            aws_sdk_emr_serverless.types.maximum_allowed_resources.serialize_json(
                value["maximum_capacity"]
            )
        )
    import aws_sdk_emr_serverless.types.date

    out["createdAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import aws_sdk_emr_serverless.types.date

    out["updatedAt"] = aws_sdk_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.serialize_json(value["tags"])
    if "auto_start_configuration" in value:
        import aws_sdk_emr_serverless.types.auto_start_config

        out["autoStartConfiguration"] = (
            aws_sdk_emr_serverless.types.auto_start_config.serialize_json(
                value["auto_start_configuration"]
            )
        )
    if "auto_stop_configuration" in value:
        import aws_sdk_emr_serverless.types.auto_stop_config

        out["autoStopConfiguration"] = (
            aws_sdk_emr_serverless.types.auto_stop_config.serialize_json(
                value["auto_stop_configuration"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_emr_serverless.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_emr_serverless.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "image_configuration" in value:
        import aws_sdk_emr_serverless.types.image_configuration

        out["imageConfiguration"] = (
            aws_sdk_emr_serverless.types.image_configuration.serialize_json(
                value["image_configuration"]
            )
        )
    if "worker_type_specifications" in value:
        import aws_sdk_emr_serverless.types.worker_type_specification_map

        out["workerTypeSpecifications"] = (
            aws_sdk_emr_serverless.types.worker_type_specification_map.serialize_json(
                value["worker_type_specifications"]
            )
        )
    if "runtime_configuration" in value:
        import aws_sdk_emr_serverless.types.configuration_list

        out["runtimeConfiguration"] = (
            aws_sdk_emr_serverless.types.configuration_list.serialize_json(
                value["runtime_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import aws_sdk_emr_serverless.types.monitoring_configuration

        out["monitoringConfiguration"] = (
            aws_sdk_emr_serverless.types.monitoring_configuration.serialize_json(
                value["monitoring_configuration"]
            )
        )
    if "disk_encryption_configuration" in value:
        import aws_sdk_emr_serverless.types.disk_encryption_configuration

        out["diskEncryptionConfiguration"] = (
            aws_sdk_emr_serverless.types.disk_encryption_configuration.serialize_json(
                value["disk_encryption_configuration"]
            )
        )
    if "interactive_configuration" in value:
        import aws_sdk_emr_serverless.types.interactive_configuration

        out["interactiveConfiguration"] = (
            aws_sdk_emr_serverless.types.interactive_configuration.serialize_json(
                value["interactive_configuration"]
            )
        )
    if "scheduler_configuration" in value:
        import aws_sdk_emr_serverless.types.scheduler_configuration

        out["schedulerConfiguration"] = (
            aws_sdk_emr_serverless.types.scheduler_configuration.serialize_json(
                value["scheduler_configuration"]
            )
        )
    if "identity_center_configuration" in value:
        import aws_sdk_emr_serverless.types.identity_center_configuration

        out["identityCenterConfiguration"] = (
            aws_sdk_emr_serverless.types.identity_center_configuration.serialize_json(
                value["identity_center_configuration"]
            )
        )
    if "job_level_cost_allocation_configuration" in value:
        import aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration

        out["jobLevelCostAllocationConfiguration"] = (
            aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration.serialize_json(
                value["job_level_cost_allocation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("Application.application_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Application.arn required")
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
    else:
        raise DeserializationError("Application.release_label required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Application.type required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("Application.state required")
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    if "initialCapacity" in data:
        import aws_sdk_emr_serverless.types.initial_capacity_config_map

        out["initial_capacity"] = (
            aws_sdk_emr_serverless.types.initial_capacity_config_map.deserialize_json(
                data["initialCapacity"]
            )
        )
    if "maximumCapacity" in data:
        import aws_sdk_emr_serverless.types.maximum_allowed_resources

        out["maximum_capacity"] = (
            aws_sdk_emr_serverless.types.maximum_allowed_resources.deserialize_json(
                data["maximumCapacity"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["created_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Application.created_at required")
    if "updatedAt" in data:
        import aws_sdk_emr_serverless.types.date

        out["updated_at"] = aws_sdk_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Application.updated_at required")
    if "tags" in data:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "autoStartConfiguration" in data:
        import aws_sdk_emr_serverless.types.auto_start_config

        out["auto_start_configuration"] = (
            aws_sdk_emr_serverless.types.auto_start_config.deserialize_json(
                data["autoStartConfiguration"]
            )
        )
    if "autoStopConfiguration" in data:
        import aws_sdk_emr_serverless.types.auto_stop_config

        out["auto_stop_configuration"] = (
            aws_sdk_emr_serverless.types.auto_stop_config.deserialize_json(
                data["autoStopConfiguration"]
            )
        )
    if "networkConfiguration" in data:
        import aws_sdk_emr_serverless.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_emr_serverless.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    if "imageConfiguration" in data:
        import aws_sdk_emr_serverless.types.image_configuration

        out["image_configuration"] = (
            aws_sdk_emr_serverless.types.image_configuration.deserialize_json(
                data["imageConfiguration"]
            )
        )
    if "workerTypeSpecifications" in data:
        import aws_sdk_emr_serverless.types.worker_type_specification_map

        out["worker_type_specifications"] = (
            aws_sdk_emr_serverless.types.worker_type_specification_map.deserialize_json(
                data["workerTypeSpecifications"]
            )
        )
    if "runtimeConfiguration" in data:
        import aws_sdk_emr_serverless.types.configuration_list

        out["runtime_configuration"] = (
            aws_sdk_emr_serverless.types.configuration_list.deserialize_json(
                data["runtimeConfiguration"]
            )
        )
    if "monitoringConfiguration" in data:
        import aws_sdk_emr_serverless.types.monitoring_configuration

        out["monitoring_configuration"] = (
            aws_sdk_emr_serverless.types.monitoring_configuration.deserialize_json(
                data["monitoringConfiguration"]
            )
        )
    if "diskEncryptionConfiguration" in data:
        import aws_sdk_emr_serverless.types.disk_encryption_configuration

        out["disk_encryption_configuration"] = (
            aws_sdk_emr_serverless.types.disk_encryption_configuration.deserialize_json(
                data["diskEncryptionConfiguration"]
            )
        )
    if "interactiveConfiguration" in data:
        import aws_sdk_emr_serverless.types.interactive_configuration

        out["interactive_configuration"] = (
            aws_sdk_emr_serverless.types.interactive_configuration.deserialize_json(
                data["interactiveConfiguration"]
            )
        )
    if "schedulerConfiguration" in data:
        import aws_sdk_emr_serverless.types.scheduler_configuration

        out["scheduler_configuration"] = (
            aws_sdk_emr_serverless.types.scheduler_configuration.deserialize_json(
                data["schedulerConfiguration"]
            )
        )
    if "identityCenterConfiguration" in data:
        import aws_sdk_emr_serverless.types.identity_center_configuration

        out["identity_center_configuration"] = (
            aws_sdk_emr_serverless.types.identity_center_configuration.deserialize_json(
                data["identityCenterConfiguration"]
            )
        )
    if "jobLevelCostAllocationConfiguration" in data:
        import aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration

        out["job_level_cost_allocation_configuration"] = (
            aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration.deserialize_json(
                data["jobLevelCostAllocationConfiguration"]
            )
        )
    return out

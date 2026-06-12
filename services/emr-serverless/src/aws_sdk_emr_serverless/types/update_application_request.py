"""Generated from Smithy shape ``com.amazonaws.emrserverless#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.architecture
    import aws_sdk_emr_serverless.types.auto_start_config
    import aws_sdk_emr_serverless.types.auto_stop_config
    import aws_sdk_emr_serverless.types.client_token
    import aws_sdk_emr_serverless.types.configuration_list
    import aws_sdk_emr_serverless.types.disk_encryption_configuration
    import aws_sdk_emr_serverless.types.identity_center_configuration_input
    import aws_sdk_emr_serverless.types.image_configuration_input
    import aws_sdk_emr_serverless.types.initial_capacity_config_map
    import aws_sdk_emr_serverless.types.interactive_configuration
    import aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration
    import aws_sdk_emr_serverless.types.maximum_allowed_resources
    import aws_sdk_emr_serverless.types.monitoring_configuration
    import aws_sdk_emr_serverless.types.network_configuration
    import aws_sdk_emr_serverless.types.release_label
    import aws_sdk_emr_serverless.types.scheduler_configuration
    import aws_sdk_emr_serverless.types.worker_type_specification_input_map


class UpdateApplicationRequest(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application to update.</p>"""
    client_token: "aws_sdk_emr_serverless.types.client_token.ClientToken"
    """<p>The client idempotency token of the application to update. Its value must be unique for each request.</p>"""
    initial_capacity: NotRequired[
        "aws_sdk_emr_serverless.types.initial_capacity_config_map.InitialCapacityConfigMap"
    ]
    """<p>The capacity to initialize when the application is updated.</p>"""
    maximum_capacity: NotRequired[
        "aws_sdk_emr_serverless.types.maximum_allowed_resources.MaximumAllowedResources"
    ]
    """<p>The maximum capacity to allocate when the application is updated. This is cumulative across all workers at any given point in time during the lifespan of the application. No new resources will be created once any one of the defined limits is hit.</p>"""
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
    architecture: NotRequired["aws_sdk_emr_serverless.types.architecture.Architecture"]
    """<p>The CPU architecture of an application.</p>"""
    image_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
    ]
    """<p>The image configuration to be used for all worker types. You can either set this parameter or <code>imageConfiguration</code> for each worker type in <code>WorkerTypeSpecificationInput</code>.</p>"""
    worker_type_specifications: NotRequired[
        "aws_sdk_emr_serverless.types.worker_type_specification_input_map.WorkerTypeSpecificationInputMap"
    ]
    """<p>The key-value pairs that specify worker type to <code>WorkerTypeSpecificationInput</code>. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include <code>Driver</code> and <code>Executor</code> for Spark applications and <code>HiveDriver</code> and <code>TezTask</code> for Hive applications. You can either set image details in this parameter for each worker type, or in <code>imageConfiguration</code> for all worker types.</p>"""
    interactive_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.interactive_configuration.InteractiveConfiguration"
    ]
    """<p>The interactive configuration object that contains new interactive use cases when the application is updated.</p>"""
    release_label: NotRequired[
        "aws_sdk_emr_serverless.types.release_label.ReleaseLabel"
    ]
    """<p>The Amazon EMR release label for the application. You can change the release label to use a different release of Amazon EMR.</p>"""
    runtime_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.configuration_list.ConfigurationList"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html\">Configuration</a> specifications to use when updating an application. Each configuration consists of a classification and properties. This configuration is applied across all the job runs submitted under the application.</p>"""
    monitoring_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The configuration setting for monitoring.</p>"""
    disk_encryption_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
    ]
    """<p>The configuration object that allows encrypting local disks.</p>"""
    scheduler_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.scheduler_configuration.SchedulerConfiguration"
    ]
    """<p>The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.</p>"""
    identity_center_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.identity_center_configuration_input.IdentityCenterConfigurationInput"
    ]
    """<p>Specifies the IAM Identity Center configuration used to enable or disable trusted identity propagation. When provided, this configuration determines how the application interacts with IAM Identity Center for user authentication and access control.</p>"""
    job_level_cost_allocation_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration.JobLevelCostAllocationConfiguration"
    ]
    """<p>The configuration object that enables job level cost allocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
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
        import aws_sdk_emr_serverless.types.image_configuration_input

        out["imageConfiguration"] = (
            aws_sdk_emr_serverless.types.image_configuration_input.serialize_json(
                value["image_configuration"]
            )
        )
    if "worker_type_specifications" in value:
        import aws_sdk_emr_serverless.types.worker_type_specification_input_map

        out["workerTypeSpecifications"] = (
            aws_sdk_emr_serverless.types.worker_type_specification_input_map.serialize_json(
                value["worker_type_specifications"]
            )
        )
    if "interactive_configuration" in value:
        import aws_sdk_emr_serverless.types.interactive_configuration

        out["interactiveConfiguration"] = (
            aws_sdk_emr_serverless.types.interactive_configuration.serialize_json(
                value["interactive_configuration"]
            )
        )
    if "release_label" in value:
        out["releaseLabel"] = value["release_label"]
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
    if "scheduler_configuration" in value:
        import aws_sdk_emr_serverless.types.scheduler_configuration

        out["schedulerConfiguration"] = (
            aws_sdk_emr_serverless.types.scheduler_configuration.serialize_json(
                value["scheduler_configuration"]
            )
        )
    if "identity_center_configuration" in value:
        import aws_sdk_emr_serverless.types.identity_center_configuration_input

        out["identityCenterConfiguration"] = (
            aws_sdk_emr_serverless.types.identity_center_configuration_input.serialize_json(
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


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateApplicationRequest.client_token required")
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
        import aws_sdk_emr_serverless.types.image_configuration_input

        out["image_configuration"] = (
            aws_sdk_emr_serverless.types.image_configuration_input.deserialize_json(
                data["imageConfiguration"]
            )
        )
    if "workerTypeSpecifications" in data:
        import aws_sdk_emr_serverless.types.worker_type_specification_input_map

        out["worker_type_specifications"] = (
            aws_sdk_emr_serverless.types.worker_type_specification_input_map.deserialize_json(
                data["workerTypeSpecifications"]
            )
        )
    if "interactiveConfiguration" in data:
        import aws_sdk_emr_serverless.types.interactive_configuration

        out["interactive_configuration"] = (
            aws_sdk_emr_serverless.types.interactive_configuration.deserialize_json(
                data["interactiveConfiguration"]
            )
        )
    if "releaseLabel" in data:
        out["release_label"] = data["releaseLabel"]
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
    if "schedulerConfiguration" in data:
        import aws_sdk_emr_serverless.types.scheduler_configuration

        out["scheduler_configuration"] = (
            aws_sdk_emr_serverless.types.scheduler_configuration.deserialize_json(
                data["schedulerConfiguration"]
            )
        )
    if "identityCenterConfiguration" in data:
        import aws_sdk_emr_serverless.types.identity_center_configuration_input

        out["identity_center_configuration"] = (
            aws_sdk_emr_serverless.types.identity_center_configuration_input.deserialize_json(
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

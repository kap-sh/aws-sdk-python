"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.initial_task_count
    import aws_sdk_sagemaker.types.instance_pool_list
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.production_variant_accelerator_type
    import aws_sdk_sagemaker.types.production_variant_capacity_reservation_config
    import aws_sdk_sagemaker.types.production_variant_container_startup_health_check_timeout_in_seconds
    import aws_sdk_sagemaker.types.production_variant_core_dump_config
    import aws_sdk_sagemaker.types.production_variant_inference_ami_version
    import aws_sdk_sagemaker.types.production_variant_instance_type
    import aws_sdk_sagemaker.types.production_variant_managed_instance_scaling
    import aws_sdk_sagemaker.types.production_variant_model_data_download_timeout_in_seconds
    import aws_sdk_sagemaker.types.production_variant_routing_config
    import aws_sdk_sagemaker.types.production_variant_serverless_config
    import aws_sdk_sagemaker.types.production_variant_ssm_access
    import aws_sdk_sagemaker.types.production_variant_volume_size_in_gb
    import aws_sdk_sagemaker.types.variant_instance_provision_timeout_in_seconds
    import aws_sdk_sagemaker.types.variant_name
    import aws_sdk_sagemaker.types.variant_weight


class ProductionVariant(TypedDict):
    variant_name: NotRequired["aws_sdk_sagemaker.types.variant_name.VariantName"]
    """<p>The name of the production variant.</p>"""
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model that you want to host. This is the name that you specified when creating the model.</p>"""
    initial_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.initial_task_count.InitialTaskCount"
    ]
    """<p>Number of instances to launch initially.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The ML compute instance type.</p>"""
    instance_pools: NotRequired[
        "aws_sdk_sagemaker.types.instance_pool_list.InstancePoolList"
    ]
    """<p>A list of instance pools for the production variant. Each instance pool specifies an instance type and its priority for provisioning. Use instance pools to configure heterogeneous endpoints that deploy models across multiple instance types.</p>"""
    variant_instance_provision_timeout_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.variant_instance_provision_timeout_in_seconds.VariantInstanceProvisionTimeoutInSeconds"
    ]
    """<p>The timeout value, in seconds, for provisioning instances for the production variant. When SageMaker encounters an insufficient capacity error while provisioning instances, it retries with the next instance pool (if configured) or waits until the timeout expires. This timeout applies only to capacity provisioning and does not include the time for model download or container startup.</p> <p>Valid values: 300 to 3600.</p>"""
    initial_variant_weight: NotRequired[
        "aws_sdk_sagemaker.types.variant_weight.VariantWeight"
    ]
    """<p>Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the <code>VariantWeight</code> to the sum of all <code>VariantWeight</code> values across all ProductionVariants. If unspecified, it defaults to 1.0. </p>"""
    accelerator_type: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_accelerator_type.ProductionVariantAcceleratorType"
    ]
    """<p>This parameter is no longer supported. Elastic Inference (EI) is no longer available.</p> <p>This parameter was used to specify the size of the EI instance to use for the production variant.</p>"""
    core_dump_config: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_core_dump_config.ProductionVariantCoreDumpConfig"
    ]
    """<p>Specifies configuration for a core dump from the model container when the process crashes.</p>"""
    serverless_config: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]
    """<p>The serverless configuration for an endpoint. Specifies a serverless endpoint configuration instead of an instance-based endpoint configuration.</p>"""
    volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_volume_size_in_gb.ProductionVariantVolumeSizeInGB"
    ]
    """<p>The size, in GB, of the ML storage volume attached to individual inference instance associated with the production variant. Currently only Amazon EBS gp2 storage volumes are supported.</p>"""
    model_data_download_timeout_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_model_data_download_timeout_in_seconds.ProductionVariantModelDataDownloadTimeoutInSeconds"
    ]
    """<p>The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this production variant.</p>"""
    container_startup_health_check_timeout_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_container_startup_health_check_timeout_in_seconds.ProductionVariantContainerStartupHealthCheckTimeoutInSeconds"
    ]
    r"""<p>The timeout value, in seconds, for your inference container to pass health check by SageMaker Hosting. For more information about health check, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests\">How Your Container Should Respond to Health Check (Ping) Requests</a>.</p>"""
    enable_ssm_access: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_ssm_access.ProductionVariantSSMAccess"
    ]
    """<p> You can use this parameter to turn on native Amazon Web Services Systems Manager (SSM) access for a production variant behind an endpoint. By default, SSM access is disabled for all production variants behind an endpoint. You can turn on or turn off SSM access for a production variant behind an existing endpoint by creating a new endpoint configuration and calling <code>UpdateEndpoint</code>. </p>"""
    managed_instance_scaling: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_managed_instance_scaling.ProductionVariantManagedInstanceScaling"
    ]
    """<p>Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic. </p>"""
    routing_config: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_routing_config.ProductionVariantRoutingConfig"
    ]
    """<p>Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.</p>"""
    inference_ami_version: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_inference_ami_version.ProductionVariantInferenceAmiVersion"
    ]
    """<p>Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions. Amazon Web Services optimizes these configurations for different machine learning workloads.</p> <p>By selecting an AMI version, you can ensure that your inference environment is compatible with specific software requirements, such as CUDA driver versions, Linux kernel versions, or Amazon Web Services Neuron driver versions.</p> <p>The AMI version names, and their configurations, are the following:</p> <dl> <dt>al2-ami-sagemaker-inference-gpu-2</dt> <dd> <ul> <li> <p>Accelerator: GPU</p> </li> <li> <p>NVIDIA driver version: 535</p> </li> <li> <p>CUDA version: 12.2</p> </li> </ul> </dd> <dt>al2-ami-sagemaker-inference-gpu-2-1</dt> <dd> <ul> <li> <p>Accelerator: GPU</p> </li> <li> <p>NVIDIA driver version: 535</p> </li> <li> <p>CUDA version: 12.2</p> </li> <li> <p>NVIDIA Container Toolkit with disabled CUDA-compat mounting</p> </li> </ul> </dd> <dt>al2-ami-sagemaker-inference-gpu-3-1</dt> <dd> <ul> <li> <p>Accelerator: GPU</p> </li> <li> <p>NVIDIA driver version: 550</p> </li> <li> <p>CUDA version: 12.4</p> </li> <li> <p>NVIDIA Container Toolkit with disabled CUDA-compat mounting</p> </li> </ul> </dd> <dt>al2023-ami-sagemaker-inference-gpu-4-1</dt> <dd> <ul> <li> <p>Accelerator: GPU</p> </li> <li> <p>NVIDIA driver version: 580</p> </li> <li> <p>CUDA version: 13.0</p> </li> <li> <p>NVIDIA Container Toolkit with disabled CUDA-compat mounting</p> </li> </ul> </dd> <dt>al2-ami-sagemaker-inference-neuron-2</dt> <dd> <ul> <li> <p>Accelerator: Inferentia2 and Trainium</p> </li> <li> <p>Neuron driver version: 2.19</p> </li> </ul> </dd> </dl>"""
    capacity_reservation_config: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_capacity_reservation_config.ProductionVariantCapacityReservationConfig"
    ]
    """<p>Settings for the capacity reservation for the compute instances that SageMaker AI reserves for an endpoint. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariant) -> dict:
    out: dict = {}
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "initial_instance_count" in value:
        out["InitialInstanceCount"] = value["initial_instance_count"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_pools" in value:
        import aws_sdk_sagemaker.types.instance_pool_list

        out["InstancePools"] = (
            aws_sdk_sagemaker.types.instance_pool_list.serialize_aws_json_1_1(
                value["instance_pools"]
            )
        )
    if "variant_instance_provision_timeout_in_seconds" in value:
        out["VariantInstanceProvisionTimeoutInSeconds"] = value[
            "variant_instance_provision_timeout_in_seconds"
        ]
    if "initial_variant_weight" in value:
        out["InitialVariantWeight"] = value["initial_variant_weight"]
    if "accelerator_type" in value:
        import aws_sdk_sagemaker.types.production_variant_accelerator_type

        out["AcceleratorType"] = (
            aws_sdk_sagemaker.types.production_variant_accelerator_type.serialize_aws_json_1_1(
                value["accelerator_type"]
            )
        )
    if "core_dump_config" in value:
        import aws_sdk_sagemaker.types.production_variant_core_dump_config

        out["CoreDumpConfig"] = (
            aws_sdk_sagemaker.types.production_variant_core_dump_config.serialize_aws_json_1_1(
                value["core_dump_config"]
            )
        )
    if "serverless_config" in value:
        import aws_sdk_sagemaker.types.production_variant_serverless_config

        out["ServerlessConfig"] = (
            aws_sdk_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["serverless_config"]
            )
        )
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "model_data_download_timeout_in_seconds" in value:
        out["ModelDataDownloadTimeoutInSeconds"] = value[
            "model_data_download_timeout_in_seconds"
        ]
    if "container_startup_health_check_timeout_in_seconds" in value:
        out["ContainerStartupHealthCheckTimeoutInSeconds"] = value[
            "container_startup_health_check_timeout_in_seconds"
        ]
    if "enable_ssm_access" in value:
        out["EnableSSMAccess"] = value["enable_ssm_access"]
    if "managed_instance_scaling" in value:
        import aws_sdk_sagemaker.types.production_variant_managed_instance_scaling

        out["ManagedInstanceScaling"] = (
            aws_sdk_sagemaker.types.production_variant_managed_instance_scaling.serialize_aws_json_1_1(
                value["managed_instance_scaling"]
            )
        )
    if "routing_config" in value:
        import aws_sdk_sagemaker.types.production_variant_routing_config

        out["RoutingConfig"] = (
            aws_sdk_sagemaker.types.production_variant_routing_config.serialize_aws_json_1_1(
                value["routing_config"]
            )
        )
    if "inference_ami_version" in value:
        import aws_sdk_sagemaker.types.production_variant_inference_ami_version

        out["InferenceAmiVersion"] = (
            aws_sdk_sagemaker.types.production_variant_inference_ami_version.serialize_aws_json_1_1(
                value["inference_ami_version"]
            )
        )
    if "capacity_reservation_config" in value:
        import aws_sdk_sagemaker.types.production_variant_capacity_reservation_config

        out["CapacityReservationConfig"] = (
            aws_sdk_sagemaker.types.production_variant_capacity_reservation_config.serialize_aws_json_1_1(
                value["capacity_reservation_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariant:
    out: ProductionVariant = {}  # type: ignore[typeddict-item]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "InitialInstanceCount" in data:
        out["initial_instance_count"] = data["InitialInstanceCount"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstancePools" in data:
        import aws_sdk_sagemaker.types.instance_pool_list

        out["instance_pools"] = (
            aws_sdk_sagemaker.types.instance_pool_list.deserialize_aws_json_1_1(
                data["InstancePools"]
            )
        )
    if "VariantInstanceProvisionTimeoutInSeconds" in data:
        out["variant_instance_provision_timeout_in_seconds"] = data[
            "VariantInstanceProvisionTimeoutInSeconds"
        ]
    if "InitialVariantWeight" in data:
        out["initial_variant_weight"] = data["InitialVariantWeight"]
    if "AcceleratorType" in data:
        import aws_sdk_sagemaker.types.production_variant_accelerator_type

        out["accelerator_type"] = (
            aws_sdk_sagemaker.types.production_variant_accelerator_type.deserialize_aws_json_1_1(
                data["AcceleratorType"]
            )
        )
    if "CoreDumpConfig" in data:
        import aws_sdk_sagemaker.types.production_variant_core_dump_config

        out["core_dump_config"] = (
            aws_sdk_sagemaker.types.production_variant_core_dump_config.deserialize_aws_json_1_1(
                data["CoreDumpConfig"]
            )
        )
    if "ServerlessConfig" in data:
        import aws_sdk_sagemaker.types.production_variant_serverless_config

        out["serverless_config"] = (
            aws_sdk_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["ServerlessConfig"]
            )
        )
    if "VolumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if "ModelDataDownloadTimeoutInSeconds" in data:
        out["model_data_download_timeout_in_seconds"] = data[
            "ModelDataDownloadTimeoutInSeconds"
        ]
    if "ContainerStartupHealthCheckTimeoutInSeconds" in data:
        out["container_startup_health_check_timeout_in_seconds"] = data[
            "ContainerStartupHealthCheckTimeoutInSeconds"
        ]
    if "EnableSSMAccess" in data:
        out["enable_ssm_access"] = data["EnableSSMAccess"]
    if "ManagedInstanceScaling" in data:
        import aws_sdk_sagemaker.types.production_variant_managed_instance_scaling

        out["managed_instance_scaling"] = (
            aws_sdk_sagemaker.types.production_variant_managed_instance_scaling.deserialize_aws_json_1_1(
                data["ManagedInstanceScaling"]
            )
        )
    if "RoutingConfig" in data:
        import aws_sdk_sagemaker.types.production_variant_routing_config

        out["routing_config"] = (
            aws_sdk_sagemaker.types.production_variant_routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
    if "InferenceAmiVersion" in data:
        import aws_sdk_sagemaker.types.production_variant_inference_ami_version

        out["inference_ami_version"] = (
            aws_sdk_sagemaker.types.production_variant_inference_ami_version.deserialize_aws_json_1_1(
                data["InferenceAmiVersion"]
            )
        )
    if "CapacityReservationConfig" in data:
        import aws_sdk_sagemaker.types.production_variant_capacity_reservation_config

        out["capacity_reservation_config"] = (
            aws_sdk_sagemaker.types.production_variant_capacity_reservation_config.deserialize_aws_json_1_1(
                data["CapacityReservationConfig"]
            )
        )
    return out

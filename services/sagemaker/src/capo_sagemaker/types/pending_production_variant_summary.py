"""Generated from Smithy shape ``com.amazonaws.sagemaker#PendingProductionVariantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.deployed_images
    import capo_sagemaker.types.instance_pool_summary_list
    import capo_sagemaker.types.production_variant_accelerator_type
    import capo_sagemaker.types.production_variant_instance_type
    import capo_sagemaker.types.production_variant_managed_instance_scaling
    import capo_sagemaker.types.production_variant_routing_config
    import capo_sagemaker.types.production_variant_serverless_config
    import capo_sagemaker.types.production_variant_status_list
    import capo_sagemaker.types.task_count
    import capo_sagemaker.types.variant_name
    import capo_sagemaker.types.variant_weight


class PendingProductionVariantSummary(TypedDict, closed=True):
    variant_name: NotRequired["capo_sagemaker.types.variant_name.VariantName"]
    """<p>The name of the variant.</p>"""
    deployed_images: NotRequired["capo_sagemaker.types.deployed_images.DeployedImages"]
    """<p>An array of <code>DeployedImage</code> objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this <code>ProductionVariant</code>.</p>"""
    current_weight: NotRequired["capo_sagemaker.types.variant_weight.VariantWeight"]
    """<p>The weight associated with the variant.</p>"""
    desired_weight: NotRequired["capo_sagemaker.types.variant_weight.VariantWeight"]
    r"""<p>The requested weight for the variant in this deployment, as specified in the endpoint configuration for the endpoint. The value is taken from the request to the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html\">CreateEndpointConfig</a> operation.</p>"""
    current_instance_count: NotRequired["capo_sagemaker.types.task_count.TaskCount"]
    """<p>The number of instances associated with the variant.</p>"""
    desired_instance_count: NotRequired["capo_sagemaker.types.task_count.TaskCount"]
    r"""<p>The number of instances requested in this deployment, as specified in the endpoint configuration for the endpoint. The value is taken from the request to the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html\">CreateEndpointConfig</a> operation.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The type of instances associated with the variant.</p>"""
    instance_pools: NotRequired[
        "capo_sagemaker.types.instance_pool_summary_list.InstancePoolSummaryList"
    ]
    """<p>A list of instance pools for the production variant. Each pool indicates the instance type and the current number of instances of that type.</p>"""
    accelerator_type: NotRequired[
        "capo_sagemaker.types.production_variant_accelerator_type.ProductionVariantAcceleratorType"
    ]
    """<p>This parameter is no longer supported. Elastic Inference (EI) is no longer available.</p> <p>This parameter was used to specify the size of the EI instance to use for the production variant.</p>"""
    variant_status: NotRequired[
        "capo_sagemaker.types.production_variant_status_list.ProductionVariantStatusList"
    ]
    """<p>The endpoint variant status which describes the current deployment stage status or operational status.</p>"""
    current_serverless_config: NotRequired[
        "capo_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]
    """<p>The serverless configuration for the endpoint.</p>"""
    desired_serverless_config: NotRequired[
        "capo_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]
    """<p>The serverless configuration requested for this deployment, as specified in the endpoint configuration for the endpoint.</p>"""
    managed_instance_scaling: NotRequired[
        "capo_sagemaker.types.production_variant_managed_instance_scaling.ProductionVariantManagedInstanceScaling"
    ]
    """<p>Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic. </p>"""
    routing_config: NotRequired[
        "capo_sagemaker.types.production_variant_routing_config.ProductionVariantRoutingConfig"
    ]
    """<p>Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingProductionVariantSummary) -> dict:
    out: dict = {}
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "deployed_images" in value:
        import capo_sagemaker.types.deployed_images

        out["DeployedImages"] = (
            capo_sagemaker.types.deployed_images.serialize_aws_json_1_1(
                value["deployed_images"]
            )
        )
    if "current_weight" in value:
        out["CurrentWeight"] = value["current_weight"]
    if "desired_weight" in value:
        out["DesiredWeight"] = value["desired_weight"]
    if "current_instance_count" in value:
        out["CurrentInstanceCount"] = value["current_instance_count"]
    if "desired_instance_count" in value:
        out["DesiredInstanceCount"] = value["desired_instance_count"]
    if "instance_type" in value:
        import capo_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_pools" in value:
        import capo_sagemaker.types.instance_pool_summary_list

        out["InstancePools"] = (
            capo_sagemaker.types.instance_pool_summary_list.serialize_aws_json_1_1(
                value["instance_pools"]
            )
        )
    if "accelerator_type" in value:
        import capo_sagemaker.types.production_variant_accelerator_type

        out["AcceleratorType"] = (
            capo_sagemaker.types.production_variant_accelerator_type.serialize_aws_json_1_1(
                value["accelerator_type"]
            )
        )
    if "variant_status" in value:
        import capo_sagemaker.types.production_variant_status_list

        out["VariantStatus"] = (
            capo_sagemaker.types.production_variant_status_list.serialize_aws_json_1_1(
                value["variant_status"]
            )
        )
    if "current_serverless_config" in value:
        import capo_sagemaker.types.production_variant_serverless_config

        out["CurrentServerlessConfig"] = (
            capo_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["current_serverless_config"]
            )
        )
    if "desired_serverless_config" in value:
        import capo_sagemaker.types.production_variant_serverless_config

        out["DesiredServerlessConfig"] = (
            capo_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["desired_serverless_config"]
            )
        )
    if "managed_instance_scaling" in value:
        import capo_sagemaker.types.production_variant_managed_instance_scaling

        out["ManagedInstanceScaling"] = (
            capo_sagemaker.types.production_variant_managed_instance_scaling.serialize_aws_json_1_1(
                value["managed_instance_scaling"]
            )
        )
    if "routing_config" in value:
        import capo_sagemaker.types.production_variant_routing_config

        out["RoutingConfig"] = (
            capo_sagemaker.types.production_variant_routing_config.serialize_aws_json_1_1(
                value["routing_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingProductionVariantSummary:
    out: PendingProductionVariantSummary = {}  # type: ignore[typeddict-item]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "DeployedImages" in data:
        import capo_sagemaker.types.deployed_images

        out["deployed_images"] = (
            capo_sagemaker.types.deployed_images.deserialize_aws_json_1_1(
                data["DeployedImages"]
            )
        )
    if "CurrentWeight" in data:
        out["current_weight"] = data["CurrentWeight"]
    if "DesiredWeight" in data:
        out["desired_weight"] = data["DesiredWeight"]
    if "CurrentInstanceCount" in data:
        out["current_instance_count"] = data["CurrentInstanceCount"]
    if "DesiredInstanceCount" in data:
        out["desired_instance_count"] = data["DesiredInstanceCount"]
    if "InstanceType" in data:
        import capo_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstancePools" in data:
        import capo_sagemaker.types.instance_pool_summary_list

        out["instance_pools"] = (
            capo_sagemaker.types.instance_pool_summary_list.deserialize_aws_json_1_1(
                data["InstancePools"]
            )
        )
    if "AcceleratorType" in data:
        import capo_sagemaker.types.production_variant_accelerator_type

        out["accelerator_type"] = (
            capo_sagemaker.types.production_variant_accelerator_type.deserialize_aws_json_1_1(
                data["AcceleratorType"]
            )
        )
    if "VariantStatus" in data:
        import capo_sagemaker.types.production_variant_status_list

        out["variant_status"] = (
            capo_sagemaker.types.production_variant_status_list.deserialize_aws_json_1_1(
                data["VariantStatus"]
            )
        )
    if "CurrentServerlessConfig" in data:
        import capo_sagemaker.types.production_variant_serverless_config

        out["current_serverless_config"] = (
            capo_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["CurrentServerlessConfig"]
            )
        )
    if "DesiredServerlessConfig" in data:
        import capo_sagemaker.types.production_variant_serverless_config

        out["desired_serverless_config"] = (
            capo_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["DesiredServerlessConfig"]
            )
        )
    if "ManagedInstanceScaling" in data:
        import capo_sagemaker.types.production_variant_managed_instance_scaling

        out["managed_instance_scaling"] = (
            capo_sagemaker.types.production_variant_managed_instance_scaling.deserialize_aws_json_1_1(
                data["ManagedInstanceScaling"]
            )
        )
    if "RoutingConfig" in data:
        import capo_sagemaker.types.production_variant_routing_config

        out["routing_config"] = (
            capo_sagemaker.types.production_variant_routing_config.deserialize_aws_json_1_1(
                data["RoutingConfig"]
            )
        )
    return out

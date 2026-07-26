"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSpecificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_compute_resource_requirements
    import capo_sagemaker.types.inference_component_container_specification_summary
    import capo_sagemaker.types.inference_component_data_cache_config_summary
    import capo_sagemaker.types.inference_component_name
    import capo_sagemaker.types.inference_component_scheduling_config
    import capo_sagemaker.types.inference_component_startup_parameters
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.production_variant_instance_type


class InferenceComponentSpecificationSummary(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The ML compute instance type associated with this inference component specification.</p>"""
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of the SageMaker AI model object that is deployed with the inference component.</p>"""
    container: NotRequired[
        "capo_sagemaker.types.inference_component_container_specification_summary.InferenceComponentContainerSpecificationSummary"
    ]
    """<p>Details about the container that provides the runtime environment for the model that is deployed with the inference component.</p>"""
    startup_parameters: NotRequired[
        "capo_sagemaker.types.inference_component_startup_parameters.InferenceComponentStartupParameters"
    ]
    """<p>Settings that take effect while the model container starts up.</p>"""
    compute_resource_requirements: NotRequired[
        "capo_sagemaker.types.inference_component_compute_resource_requirements.InferenceComponentComputeResourceRequirements"
    ]
    """<p>The compute resources allocated to run the model, plus any adapter models, that you assign to the inference component.</p>"""
    base_inference_component_name: NotRequired[
        "capo_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of the base inference component that contains this inference component.</p>"""
    data_cache_config: NotRequired[
        "capo_sagemaker.types.inference_component_data_cache_config_summary.InferenceComponentDataCacheConfigSummary"
    ]
    """<p>Settings that affect how the inference component caches data.</p>"""
    scheduling_config: NotRequired[
        "capo_sagemaker.types.inference_component_scheduling_config.InferenceComponentSchedulingConfig"
    ]
    """<p>The scheduling configuration that determines how inference component copies are placed across available instances when copies are added or removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSpecificationSummary) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "container" in value:
        import capo_sagemaker.types.inference_component_container_specification_summary

        out["Container"] = (
            capo_sagemaker.types.inference_component_container_specification_summary.serialize_aws_json_1_1(
                value["container"]
            )
        )
    if "startup_parameters" in value:
        import capo_sagemaker.types.inference_component_startup_parameters

        out["StartupParameters"] = (
            capo_sagemaker.types.inference_component_startup_parameters.serialize_aws_json_1_1(
                value["startup_parameters"]
            )
        )
    if "compute_resource_requirements" in value:
        import capo_sagemaker.types.inference_component_compute_resource_requirements

        out["ComputeResourceRequirements"] = (
            capo_sagemaker.types.inference_component_compute_resource_requirements.serialize_aws_json_1_1(
                value["compute_resource_requirements"]
            )
        )
    if "base_inference_component_name" in value:
        out["BaseInferenceComponentName"] = value["base_inference_component_name"]
    if "data_cache_config" in value:
        import capo_sagemaker.types.inference_component_data_cache_config_summary

        out["DataCacheConfig"] = (
            capo_sagemaker.types.inference_component_data_cache_config_summary.serialize_aws_json_1_1(
                value["data_cache_config"]
            )
        )
    if "scheduling_config" in value:
        import capo_sagemaker.types.inference_component_scheduling_config

        out["SchedulingConfig"] = (
            capo_sagemaker.types.inference_component_scheduling_config.serialize_aws_json_1_1(
                value["scheduling_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentSpecificationSummary:
    out: InferenceComponentSpecificationSummary = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import capo_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "Container" in data:
        import capo_sagemaker.types.inference_component_container_specification_summary

        out["container"] = (
            capo_sagemaker.types.inference_component_container_specification_summary.deserialize_aws_json_1_1(
                data["Container"]
            )
        )
    if "StartupParameters" in data:
        import capo_sagemaker.types.inference_component_startup_parameters

        out["startup_parameters"] = (
            capo_sagemaker.types.inference_component_startup_parameters.deserialize_aws_json_1_1(
                data["StartupParameters"]
            )
        )
    if "ComputeResourceRequirements" in data:
        import capo_sagemaker.types.inference_component_compute_resource_requirements

        out["compute_resource_requirements"] = (
            capo_sagemaker.types.inference_component_compute_resource_requirements.deserialize_aws_json_1_1(
                data["ComputeResourceRequirements"]
            )
        )
    if "BaseInferenceComponentName" in data:
        out["base_inference_component_name"] = data["BaseInferenceComponentName"]
    if "DataCacheConfig" in data:
        import capo_sagemaker.types.inference_component_data_cache_config_summary

        out["data_cache_config"] = (
            capo_sagemaker.types.inference_component_data_cache_config_summary.deserialize_aws_json_1_1(
                data["DataCacheConfig"]
            )
        )
    if "SchedulingConfig" in data:
        import capo_sagemaker.types.inference_component_scheduling_config

        out["scheduling_config"] = (
            capo_sagemaker.types.inference_component_scheduling_config.deserialize_aws_json_1_1(
                data["SchedulingConfig"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_compute_resource_requirements
    import capo_sagemaker.types.inference_component_container_specification
    import capo_sagemaker.types.inference_component_data_cache_config
    import capo_sagemaker.types.inference_component_name
    import capo_sagemaker.types.inference_component_scheduling_config
    import capo_sagemaker.types.inference_component_startup_parameters
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.production_variant_instance_type


class InferenceComponentSpecification(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The ML compute instance type for the inference component specification. Specifies which instance type this specification applies to. Required when using the <code>Specifications</code> parameter with multiple entries.</p>"""
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of an existing SageMaker AI model object in your account that you want to deploy with the inference component.</p>"""
    container: NotRequired[
        "capo_sagemaker.types.inference_component_container_specification.InferenceComponentContainerSpecification"
    ]
    """<p>Defines a container that provides the runtime environment for a model that you deploy with an inference component.</p>"""
    startup_parameters: NotRequired[
        "capo_sagemaker.types.inference_component_startup_parameters.InferenceComponentStartupParameters"
    ]
    """<p>Settings that take effect while the model container starts up.</p>"""
    compute_resource_requirements: NotRequired[
        "capo_sagemaker.types.inference_component_compute_resource_requirements.InferenceComponentComputeResourceRequirements"
    ]
    """<p>The compute resources allocated to run the model, plus any adapter models, that you assign to the inference component.</p> <p>Omit this parameter if your request is meant to create an adapter inference component. An adapter inference component is loaded by a base inference component, and it uses the compute resources of the base inference component.</p>"""
    base_inference_component_name: NotRequired[
        "capo_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of an existing inference component that is to contain the inference component that you're creating with your request.</p> <p>Specify this parameter only if your request is meant to create an adapter inference component. An adapter inference component contains the path to an adapter model. The purpose of the adapter model is to tailor the inference output of a base foundation model, which is hosted by the base inference component. The adapter inference component uses the compute resources that you assigned to the base inference component.</p> <p>When you create an adapter inference component, use the <code>Container</code> parameter to specify the location of the adapter artifacts. In the parameter value, use the <code>ArtifactUrl</code> parameter of the <code>InferenceComponentContainerSpecification</code> data type.</p> <p>Before you can create an adapter inference component, you must have an existing inference component that contains the foundation model that you want to adapt.</p>"""
    data_cache_config: NotRequired[
        "capo_sagemaker.types.inference_component_data_cache_config.InferenceComponentDataCacheConfig"
    ]
    """<p>Settings that affect how the inference component caches data.</p>"""
    scheduling_config: NotRequired[
        "capo_sagemaker.types.inference_component_scheduling_config.InferenceComponentSchedulingConfig"
    ]
    """<p>The scheduling configuration that determines how inference component copies are placed across available instances when copies are added or removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSpecification) -> dict:
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
        import capo_sagemaker.types.inference_component_container_specification

        out["Container"] = (
            capo_sagemaker.types.inference_component_container_specification.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.inference_component_data_cache_config

        out["DataCacheConfig"] = (
            capo_sagemaker.types.inference_component_data_cache_config.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentSpecification:
    out: InferenceComponentSpecification = {}  # type: ignore[typeddict-item]
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
        import capo_sagemaker.types.inference_component_container_specification

        out["container"] = (
            capo_sagemaker.types.inference_component_container_specification.deserialize_aws_json_1_1(
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
        import capo_sagemaker.types.inference_component_data_cache_config

        out["data_cache_config"] = (
            capo_sagemaker.types.inference_component_data_cache_config.deserialize_aws_json_1_1(
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

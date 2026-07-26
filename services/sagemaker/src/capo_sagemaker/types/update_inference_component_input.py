"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateInferenceComponentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_deployment_config
    import capo_sagemaker.types.inference_component_name
    import capo_sagemaker.types.inference_component_runtime_config
    import capo_sagemaker.types.inference_component_specification
    import capo_sagemaker.types.inference_component_specification_list


class UpdateInferenceComponentInput(TypedDict, closed=True):
    inference_component_name: NotRequired[
        "capo_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of the inference component.</p>"""
    specification: NotRequired[
        "capo_sagemaker.types.inference_component_specification.InferenceComponentSpecification"
    ]
    """<p>Details about the resources to deploy with this inference component, including the model, container, and compute resources.</p>"""
    specifications: NotRequired[
        "capo_sagemaker.types.inference_component_specification_list.InferenceComponentSpecificationList"
    ]
    """<p>A list of specification objects for the inference component, one per instance type. Use this parameter when you want to specify different model or resource configurations for the inference component on each instance type. You can use either this parameter or the singular <code>Specification</code> parameter, but not both.</p>"""
    runtime_config: NotRequired[
        "capo_sagemaker.types.inference_component_runtime_config.InferenceComponentRuntimeConfig"
    ]
    """<p>Runtime settings for a model that is deployed with an inference component.</p>"""
    deployment_config: NotRequired[
        "capo_sagemaker.types.inference_component_deployment_config.InferenceComponentDeploymentConfig"
    ]
    """<p>The deployment configuration for the inference component. The configuration contains the desired deployment strategy and rollback settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInferenceComponentInput) -> dict:
    out: dict = {}
    if "inference_component_name" in value:
        out["InferenceComponentName"] = value["inference_component_name"]
    if "specification" in value:
        import capo_sagemaker.types.inference_component_specification

        out["Specification"] = (
            capo_sagemaker.types.inference_component_specification.serialize_aws_json_1_1(
                value["specification"]
            )
        )
    if "specifications" in value:
        import capo_sagemaker.types.inference_component_specification_list

        out["Specifications"] = (
            capo_sagemaker.types.inference_component_specification_list.serialize_aws_json_1_1(
                value["specifications"]
            )
        )
    if "runtime_config" in value:
        import capo_sagemaker.types.inference_component_runtime_config

        out["RuntimeConfig"] = (
            capo_sagemaker.types.inference_component_runtime_config.serialize_aws_json_1_1(
                value["runtime_config"]
            )
        )
    if "deployment_config" in value:
        import capo_sagemaker.types.inference_component_deployment_config

        out["DeploymentConfig"] = (
            capo_sagemaker.types.inference_component_deployment_config.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInferenceComponentInput:
    out: UpdateInferenceComponentInput = {}  # type: ignore[typeddict-item]
    if "InferenceComponentName" in data:
        out["inference_component_name"] = data["InferenceComponentName"]
    if "Specification" in data:
        import capo_sagemaker.types.inference_component_specification

        out["specification"] = (
            capo_sagemaker.types.inference_component_specification.deserialize_aws_json_1_1(
                data["Specification"]
            )
        )
    if "Specifications" in data:
        import capo_sagemaker.types.inference_component_specification_list

        out["specifications"] = (
            capo_sagemaker.types.inference_component_specification_list.deserialize_aws_json_1_1(
                data["Specifications"]
            )
        )
    if "RuntimeConfig" in data:
        import capo_sagemaker.types.inference_component_runtime_config

        out["runtime_config"] = (
            capo_sagemaker.types.inference_component_runtime_config.deserialize_aws_json_1_1(
                data["RuntimeConfig"]
            )
        )
    if "DeploymentConfig" in data:
        import capo_sagemaker.types.inference_component_deployment_config

        out["deployment_config"] = (
            capo_sagemaker.types.inference_component_deployment_config.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateInferenceExperimentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_experiment_data_storage_config
    import capo_sagemaker.types.inference_experiment_description
    import capo_sagemaker.types.inference_experiment_name
    import capo_sagemaker.types.inference_experiment_schedule
    import capo_sagemaker.types.model_variant_config_list
    import capo_sagemaker.types.shadow_mode_config


class UpdateInferenceExperimentRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name of the inference experiment to be updated.</p>"""
    schedule: NotRequired[
        "capo_sagemaker.types.inference_experiment_schedule.InferenceExperimentSchedule"
    ]
    """<p> The duration for which the inference experiment will run. If the status of the inference experiment is <code>Created</code>, then you can update both the start and end dates. If the status of the inference experiment is <code>Running</code>, then you can update only the end date. </p>"""
    description: NotRequired[
        "capo_sagemaker.types.inference_experiment_description.InferenceExperimentDescription"
    ]
    """<p>The description of the inference experiment.</p>"""
    model_variants: NotRequired[
        "capo_sagemaker.types.model_variant_config_list.ModelVariantConfigList"
    ]
    """<p> An array of <code>ModelVariantConfig</code> objects. There is one for each variant, whose infrastructure configuration you want to update. </p>"""
    data_storage_config: NotRequired[
        "capo_sagemaker.types.inference_experiment_data_storage_config.InferenceExperimentDataStorageConfig"
    ]
    """<p>The Amazon S3 location and configuration for storing inference request and response data.</p>"""
    shadow_mode_config: NotRequired[
        "capo_sagemaker.types.shadow_mode_config.ShadowModeConfig"
    ]
    """<p> The configuration of <code>ShadowMode</code> inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInferenceExperimentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "schedule" in value:
        import capo_sagemaker.types.inference_experiment_schedule

        out["Schedule"] = (
            capo_sagemaker.types.inference_experiment_schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "model_variants" in value:
        import capo_sagemaker.types.model_variant_config_list

        out["ModelVariants"] = (
            capo_sagemaker.types.model_variant_config_list.serialize_aws_json_1_1(
                value["model_variants"]
            )
        )
    if "data_storage_config" in value:
        import capo_sagemaker.types.inference_experiment_data_storage_config

        out["DataStorageConfig"] = (
            capo_sagemaker.types.inference_experiment_data_storage_config.serialize_aws_json_1_1(
                value["data_storage_config"]
            )
        )
    if "shadow_mode_config" in value:
        import capo_sagemaker.types.shadow_mode_config

        out["ShadowModeConfig"] = (
            capo_sagemaker.types.shadow_mode_config.serialize_aws_json_1_1(
                value["shadow_mode_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInferenceExperimentRequest:
    out: UpdateInferenceExperimentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Schedule" in data:
        import capo_sagemaker.types.inference_experiment_schedule

        out["schedule"] = (
            capo_sagemaker.types.inference_experiment_schedule.deserialize_aws_json_1_1(
                data["Schedule"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ModelVariants" in data:
        import capo_sagemaker.types.model_variant_config_list

        out["model_variants"] = (
            capo_sagemaker.types.model_variant_config_list.deserialize_aws_json_1_1(
                data["ModelVariants"]
            )
        )
    if "DataStorageConfig" in data:
        import capo_sagemaker.types.inference_experiment_data_storage_config

        out["data_storage_config"] = (
            capo_sagemaker.types.inference_experiment_data_storage_config.deserialize_aws_json_1_1(
                data["DataStorageConfig"]
            )
        )
    if "ShadowModeConfig" in data:
        import capo_sagemaker.types.shadow_mode_config

        out["shadow_mode_config"] = (
            capo_sagemaker.types.shadow_mode_config.deserialize_aws_json_1_1(
                data["ShadowModeConfig"]
            )
        )
    return out

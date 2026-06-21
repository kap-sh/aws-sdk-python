"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "TrainingJob",
    "Experiment",
    "ExperimentTrial",
    "ExperimentTrialComponent",
    "Endpoint",
    "Model",
    "ModelPackage",
    "ModelPackageGroup",
    "Pipeline",
    "PipelineExecution",
    "FeatureGroup",
    "FeatureMetadata",
    "Image",
    "ImageVersion",
    "Project",
    "HyperParameterTuningJob",
    "ModelCard",
    "PipelineVersion",
    "Job",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    return cast(ResourceType, data)

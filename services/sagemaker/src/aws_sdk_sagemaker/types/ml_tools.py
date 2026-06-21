"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlTools``."""

from typing import Literal, TypeAlias, cast

MlTools: TypeAlias = Literal[
    "DataWrangler",
    "FeatureStore",
    "EmrClusters",
    "AutoMl",
    "Experiments",
    "Training",
    "ModelEvaluation",
    "Pipelines",
    "Models",
    "JumpStart",
    "InferenceRecommender",
    "Endpoints",
    "Projects",
    "InferenceOptimization",
    "PerformanceEvaluation",
    "LakeraGuard",
    "Comet",
    "DeepchecksLLMEvaluation",
    "Fiddler",
    "HyperPodClusters",
    "RunningInstances",
    "Datasets",
    "Evaluators",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MlTools) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MlTools:
    return cast(MlTools, data)

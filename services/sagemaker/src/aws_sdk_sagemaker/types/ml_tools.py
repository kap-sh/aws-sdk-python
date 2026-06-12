"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlTools``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: MlTools) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MlTools:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MlTools value: {data!r}")
    return cast(MlTools, data)

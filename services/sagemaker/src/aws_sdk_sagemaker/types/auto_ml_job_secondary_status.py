"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobSecondaryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLJobSecondaryStatus: TypeAlias = Literal[
    "Starting",
    "MaxCandidatesReached",
    "Failed",
    "Stopped",
    "MaxAutoMLJobRuntimeReached",
    "Stopping",
    "CandidateDefinitionsGenerated",
    "Completed",
    "ExplainabilityError",
    "DeployingModel",
    "ModelDeploymentError",
    "GeneratingModelInsightsReport",
    "ModelInsightsError",
    "AnalyzingData",
    "FeatureEngineering",
    "ModelTuning",
    "GeneratingExplainabilityReport",
    "TrainingModels",
    "PreTraining",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Starting",
        "MaxCandidatesReached",
        "Failed",
        "Stopped",
        "MaxAutoMLJobRuntimeReached",
        "Stopping",
        "CandidateDefinitionsGenerated",
        "Completed",
        "ExplainabilityError",
        "DeployingModel",
        "ModelDeploymentError",
        "GeneratingModelInsightsReport",
        "ModelInsightsError",
        "AnalyzingData",
        "FeatureEngineering",
        "ModelTuning",
        "GeneratingExplainabilityReport",
        "TrainingModels",
        "PreTraining",
    )
)


def serialize_aws_json_1_1(value: AutoMLJobSecondaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLJobSecondaryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLJobSecondaryStatus value: {data!r}")
    return cast(AutoMLJobSecondaryStatus, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobSecondaryStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: AutoMLJobSecondaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLJobSecondaryStatus:
    return cast(AutoMLJobSecondaryStatus, data)

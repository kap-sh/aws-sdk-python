"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.candidate_definition_notebook_location
    import aws_sdk_sagemaker.types.data_exploration_notebook_location


class AutoMLJobArtifacts(TypedDict, closed=True):
    candidate_definition_notebook_location: NotRequired[
        "aws_sdk_sagemaker.types.candidate_definition_notebook_location.CandidateDefinitionNotebookLocation"
    ]
    """<p>The URL of the notebook location.</p>"""
    data_exploration_notebook_location: NotRequired[
        "aws_sdk_sagemaker.types.data_exploration_notebook_location.DataExplorationNotebookLocation"
    ]
    """<p>The URL of the notebook location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobArtifacts) -> dict:
    out: dict = {}
    if "candidate_definition_notebook_location" in value:
        out["CandidateDefinitionNotebookLocation"] = value[
            "candidate_definition_notebook_location"
        ]
    if "data_exploration_notebook_location" in value:
        out["DataExplorationNotebookLocation"] = value[
            "data_exploration_notebook_location"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobArtifacts:
    out: AutoMLJobArtifacts = {}  # type: ignore[typeddict-item]
    if "CandidateDefinitionNotebookLocation" in data:
        out["candidate_definition_notebook_location"] = data[
            "CandidateDefinitionNotebookLocation"
        ]
    if "DataExplorationNotebookLocation" in data:
        out["data_exploration_notebook_location"] = data[
            "DataExplorationNotebookLocation"
        ]
    return out

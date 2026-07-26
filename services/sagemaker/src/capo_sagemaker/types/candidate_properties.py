"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.candidate_artifact_locations
    import capo_sagemaker.types.metric_data_list


class CandidateProperties(TypedDict, closed=True):
    candidate_artifact_locations: NotRequired[
        "capo_sagemaker.types.candidate_artifact_locations.CandidateArtifactLocations"
    ]
    """<p>The Amazon S3 prefix to the artifacts generated for an AutoML candidate.</p>"""
    candidate_metrics: NotRequired[
        "capo_sagemaker.types.metric_data_list.MetricDataList"
    ]
    """<p>Information about the candidate metrics for an AutoML job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateProperties) -> dict:
    out: dict = {}
    if "candidate_artifact_locations" in value:
        import capo_sagemaker.types.candidate_artifact_locations

        out["CandidateArtifactLocations"] = (
            capo_sagemaker.types.candidate_artifact_locations.serialize_aws_json_1_1(
                value["candidate_artifact_locations"]
            )
        )
    if "candidate_metrics" in value:
        import capo_sagemaker.types.metric_data_list

        out["CandidateMetrics"] = (
            capo_sagemaker.types.metric_data_list.serialize_aws_json_1_1(
                value["candidate_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CandidateProperties:
    out: CandidateProperties = {}  # type: ignore[typeddict-item]
    if "CandidateArtifactLocations" in data:
        import capo_sagemaker.types.candidate_artifact_locations

        out["candidate_artifact_locations"] = (
            capo_sagemaker.types.candidate_artifact_locations.deserialize_aws_json_1_1(
                data["CandidateArtifactLocations"]
            )
        )
    if "CandidateMetrics" in data:
        import capo_sagemaker.types.metric_data_list

        out["candidate_metrics"] = (
            capo_sagemaker.types.metric_data_list.deserialize_aws_json_1_1(
                data["CandidateMetrics"]
            )
        )
    return out

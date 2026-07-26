"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDominantLanguageDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.dominant_language_detection_job_properties_list
    import capo_comprehend.types.string


class ListDominantLanguageDetectionJobsResponse(TypedDict, closed=True):
    dominant_language_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.dominant_language_detection_job_properties_list.DominantLanguageDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDominantLanguageDetectionJobsResponse) -> dict:
    out: dict = {}
    if "dominant_language_detection_job_properties_list" in value:
        import capo_comprehend.types.dominant_language_detection_job_properties_list

        out["DominantLanguageDetectionJobPropertiesList"] = (
            capo_comprehend.types.dominant_language_detection_job_properties_list.serialize_aws_json_1_1(
                value["dominant_language_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDominantLanguageDetectionJobsResponse:
    out: ListDominantLanguageDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if "DominantLanguageDetectionJobPropertiesList" in data:
        import capo_comprehend.types.dominant_language_detection_job_properties_list

        out["dominant_language_detection_job_properties_list"] = (
            capo_comprehend.types.dominant_language_detection_job_properties_list.deserialize_aws_json_1_1(
                data["DominantLanguageDetectionJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

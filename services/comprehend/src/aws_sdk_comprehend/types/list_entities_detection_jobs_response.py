"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntitiesDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entities_detection_job_properties_list
    import aws_sdk_comprehend.types.string


class ListEntitiesDetectionJobsResponse(TypedDict, closed=True):
    entities_detection_job_properties_list: NotRequired[
        "aws_sdk_comprehend.types.entities_detection_job_properties_list.EntitiesDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitiesDetectionJobsResponse) -> dict:
    out: dict = {}
    if "entities_detection_job_properties_list" in value:
        import aws_sdk_comprehend.types.entities_detection_job_properties_list

        out["EntitiesDetectionJobPropertiesList"] = (
            aws_sdk_comprehend.types.entities_detection_job_properties_list.serialize_aws_json_1_1(
                value["entities_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitiesDetectionJobsResponse:
    out: ListEntitiesDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if "EntitiesDetectionJobPropertiesList" in data:
        import aws_sdk_comprehend.types.entities_detection_job_properties_list

        out["entities_detection_job_properties_list"] = (
            aws_sdk_comprehend.types.entities_detection_job_properties_list.deserialize_aws_json_1_1(
                data["EntitiesDetectionJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

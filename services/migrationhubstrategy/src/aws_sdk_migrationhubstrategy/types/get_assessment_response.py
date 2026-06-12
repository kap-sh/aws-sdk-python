"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetAssessmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.assessment_targets
    import aws_sdk_migrationhubstrategy.types.async_task_id
    import aws_sdk_migrationhubstrategy.types.data_collection_details


class GetAssessmentResponse(TypedDict):
    id: NotRequired["aws_sdk_migrationhubstrategy.types.async_task_id.AsyncTaskId"]
    """<p> The ID for the specific assessment task. </p>"""
    data_collection_details: NotRequired[
        "aws_sdk_migrationhubstrategy.types.data_collection_details.DataCollectionDetails"
    ]
    """<p> Detailed information about the assessment. </p>"""
    assessment_targets: NotRequired[
        "aws_sdk_migrationhubstrategy.types.assessment_targets.AssessmentTargets"
    ]
    """<p>List of criteria for assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data_collection_details" in value:
        import aws_sdk_migrationhubstrategy.types.data_collection_details

        out["dataCollectionDetails"] = (
            aws_sdk_migrationhubstrategy.types.data_collection_details.serialize_json(
                value["data_collection_details"]
            )
        )
    if "assessment_targets" in value:
        import aws_sdk_migrationhubstrategy.types.assessment_targets

        out["assessmentTargets"] = (
            aws_sdk_migrationhubstrategy.types.assessment_targets.serialize_json(
                value["assessment_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentResponse:
    out: GetAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "dataCollectionDetails" in data:
        import aws_sdk_migrationhubstrategy.types.data_collection_details

        out["data_collection_details"] = (
            aws_sdk_migrationhubstrategy.types.data_collection_details.deserialize_json(
                data["dataCollectionDetails"]
            )
        )
    if "assessmentTargets" in data:
        import aws_sdk_migrationhubstrategy.types.assessment_targets

        out["assessment_targets"] = (
            aws_sdk_migrationhubstrategy.types.assessment_targets.deserialize_json(
                data["assessmentTargets"]
            )
        )
    return out

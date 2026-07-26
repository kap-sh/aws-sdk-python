"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.assessment_targets
    import capo_migrationhubstrategy.types.async_task_id
    import capo_migrationhubstrategy.types.data_collection_details


class GetAssessmentResponse(TypedDict, closed=True):
    id: NotRequired["capo_migrationhubstrategy.types.async_task_id.AsyncTaskId"]
    """<p> The ID for the specific assessment task. </p>"""
    data_collection_details: NotRequired[
        "capo_migrationhubstrategy.types.data_collection_details.DataCollectionDetails"
    ]
    """<p> Detailed information about the assessment. </p>"""
    assessment_targets: NotRequired[
        "capo_migrationhubstrategy.types.assessment_targets.AssessmentTargets"
    ]
    """<p>List of criteria for assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "data_collection_details" in value:
        import capo_migrationhubstrategy.types.data_collection_details

        out["dataCollectionDetails"] = (
            capo_migrationhubstrategy.types.data_collection_details.serialize_json(
                value["data_collection_details"]
            )
        )
    if "assessment_targets" in value:
        import capo_migrationhubstrategy.types.assessment_targets

        out["assessmentTargets"] = (
            capo_migrationhubstrategy.types.assessment_targets.serialize_json(
                value["assessment_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssessmentResponse:
    out: GetAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "dataCollectionDetails" in data:
        import capo_migrationhubstrategy.types.data_collection_details

        out["data_collection_details"] = (
            capo_migrationhubstrategy.types.data_collection_details.deserialize_json(
                data["dataCollectionDetails"]
            )
        )
    if "assessmentTargets" in data:
        import capo_migrationhubstrategy.types.assessment_targets

        out["assessment_targets"] = (
            capo_migrationhubstrategy.types.assessment_targets.deserialize_json(
                data["assessmentTargets"]
            )
        )
    return out

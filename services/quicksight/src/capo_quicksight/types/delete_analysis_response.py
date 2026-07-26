"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.timestamp


class DeleteAnalysisResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the deleted analysis.</p>"""
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the deleted analysis.</p>"""
    deletion_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the analysis is scheduled to be deleted.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAnalysisResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "deletion_time" in value:
        import capo_quicksight.types.timestamp

        out["DeletionTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["deletion_time"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteAnalysisResponse:
    out: DeleteAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "DeletionTime" in data:
        import capo_quicksight.types.timestamp

        out["deletion_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["DeletionTime"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#RestoreAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.folder_arn_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class RestoreAnalysisResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the analysis that you're restoring.</p>"""
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis that you're restoring. </p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    restoration_failed_folder_arns: NotRequired[
        "capo_quicksight.types.folder_arn_list.FolderArnList"
    ]
    """<p>A list of folder arns thatthe analysis failed to be restored to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreAnalysisResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "restoration_failed_folder_arns" in value:
        import capo_quicksight.types.folder_arn_list

        out["RestorationFailedFolderArns"] = (
            capo_quicksight.types.folder_arn_list.serialize_json(
                value["restoration_failed_folder_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> RestoreAnalysisResponse:
    out: RestoreAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "RestorationFailedFolderArns" in data:
        import capo_quicksight.types.folder_arn_list

        out["restoration_failed_folder_arns"] = (
            capo_quicksight.types.folder_arn_list.deserialize_json(
                data["RestorationFailedFolderArns"]
            )
        )
    return out

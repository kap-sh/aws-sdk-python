"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateAnalysisResponse(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the analysis that you're updating.</p>"""
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis.</p>"""
    update_status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The update status of the last update that was made to the analysis.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalysisResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "update_status" in value:
        import capo_quicksight.types.resource_status

        out["UpdateStatus"] = capo_quicksight.types.resource_status.serialize_json(
            value["update_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateAnalysisResponse:
    out: UpdateAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "UpdateStatus" in data:
        import capo_quicksight.types.resource_status

        out["update_status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["UpdateStatus"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

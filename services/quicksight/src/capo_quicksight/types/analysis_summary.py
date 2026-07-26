"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.timestamp


class AnalysisSummary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the analysis.</p>"""
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis. This ID displays in the URL.</p>"""
    name: NotRequired["capo_quicksight.types.analysis_name.AnalysisName"]
    """<p>The name of the analysis. This name is displayed in the Quick Sight console. </p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The last known status for the analysis.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the analysis was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the analysis was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisSummary:
    out: AnalysisSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out

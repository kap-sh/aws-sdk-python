"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Result``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.analysis_status_union
    import capo_migrationhubstrategy.types.analysis_type
    import capo_migrationhubstrategy.types.antipattern_report_result_list
    import capo_migrationhubstrategy.types.status_message


class Result(TypedDict, closed=True):
    analysis_type: NotRequired[
        "capo_migrationhubstrategy.types.analysis_type.AnalysisType"
    ]
    """<p>The error in server analysis.</p>"""
    analysis_status: NotRequired[
        "capo_migrationhubstrategy.types.analysis_status_union.AnalysisStatusUnion"
    ]
    """<p>The error in server analysis.</p>"""
    status_message: NotRequired[
        "capo_migrationhubstrategy.types.status_message.StatusMessage"
    ]
    """<p>The error in server analysis.</p>"""
    antipattern_report_result_list: NotRequired[
        "capo_migrationhubstrategy.types.antipattern_report_result_list.AntipatternReportResultList"
    ]
    """<p>The error in server analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Result) -> dict:
    out: dict = {}
    if "analysis_type" in value:
        out["analysisType"] = value["analysis_type"]
    if "analysis_status" in value:
        import capo_migrationhubstrategy.types.analysis_status_union

        out["analysisStatus"] = (
            capo_migrationhubstrategy.types.analysis_status_union.serialize_json(
                value["analysis_status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "antipattern_report_result_list" in value:
        import capo_migrationhubstrategy.types.antipattern_report_result_list

        out["antipatternReportResultList"] = (
            capo_migrationhubstrategy.types.antipattern_report_result_list.serialize_json(
                value["antipattern_report_result_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> Result:
    out: Result = {}  # type: ignore[typeddict-item]
    if "analysisType" in data:
        out["analysis_type"] = data["analysisType"]
    if "analysisStatus" in data:
        import capo_migrationhubstrategy.types.analysis_status_union

        out["analysis_status"] = (
            capo_migrationhubstrategy.types.analysis_status_union.deserialize_json(
                data["analysisStatus"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "antipatternReportResultList" in data:
        import capo_migrationhubstrategy.types.antipattern_report_result_list

        out["antipattern_report_result_list"] = (
            capo_migrationhubstrategy.types.antipattern_report_result_list.deserialize_json(
                data["antipatternReportResultList"]
            )
        )
    return out

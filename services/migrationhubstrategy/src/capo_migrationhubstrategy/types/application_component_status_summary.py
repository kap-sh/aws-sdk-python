"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.src_code_or_db_analysis_status


class ApplicationComponentStatusSummary(TypedDict, closed=True):
    src_code_or_db_analysis_status: NotRequired[
        "capo_migrationhubstrategy.types.src_code_or_db_analysis_status.SrcCodeOrDbAnalysisStatus"
    ]
    """<p>The status of database analysis.</p>"""
    count: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p>The number of application components successfully analyzed, partially successful or failed analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentStatusSummary) -> dict:
    out: dict = {}
    if "src_code_or_db_analysis_status" in value:
        out["srcCodeOrDbAnalysisStatus"] = value["src_code_or_db_analysis_status"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ApplicationComponentStatusSummary:
    out: ApplicationComponentStatusSummary = {}  # type: ignore[typeddict-item]
    if "srcCodeOrDbAnalysisStatus" in data:
        out["src_code_or_db_analysis_status"] = data["srcCodeOrDbAnalysisStatus"]
    if "count" in data:
        out["count"] = data["count"]
    return out

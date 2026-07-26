"""Generated from Smithy shape ``com.amazonaws.artifact#GetReportMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.report_id
    import capo_artifact.types.version_attribute


class GetReportMetadataRequest(TypedDict, closed=True):
    report_id: "capo_artifact.types.report_id.ReportId"
    """<p>Unique resource ID for the report resource.</p>"""
    report_version: NotRequired[
        "capo_artifact.types.version_attribute.VersionAttribute"
    ]
    """<p>Version for the report resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReportMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReportMetadataRequest:
    out: GetReportMetadataRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCisScanReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_report_status


class GetCisScanReportResponse(TypedDict, closed=True):
    url: NotRequired["str"]
    """<p> The URL where a PDF or CSV of the CIS scan report can be downloaded. </p>"""
    status: NotRequired["aws_sdk_inspector2.types.cis_report_status.CisReportStatus"]
    """<p>The status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCisScanReportResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "status" in value:
        import aws_sdk_inspector2.types.cis_report_status

        out["status"] = aws_sdk_inspector2.types.cis_report_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetCisScanReportResponse:
    out: GetCisScanReportResponse = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    if "status" in data:
        import aws_sdk_inspector2.types.cis_report_status

        out["status"] = aws_sdk_inspector2.types.cis_report_status.deserialize_json(
            data["status"]
        )
    return out

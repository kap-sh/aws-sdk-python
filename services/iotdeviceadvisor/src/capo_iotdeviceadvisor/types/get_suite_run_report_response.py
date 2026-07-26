"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteRunReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.qualification_report_download_url


class GetSuiteRunReportResponse(TypedDict, closed=True):
    qualification_report_download_url: NotRequired[
        "capo_iotdeviceadvisor.types.qualification_report_download_url.QualificationReportDownloadUrl"
    ]
    """<p>Download URL of the qualification report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuiteRunReportResponse) -> dict:
    out: dict = {}
    if "qualification_report_download_url" in value:
        out["qualificationReportDownloadUrl"] = value[
            "qualification_report_download_url"
        ]
    return out


def deserialize_json(data: dict) -> GetSuiteRunReportResponse:
    out: GetSuiteRunReportResponse = {}  # type: ignore[typeddict-item]
    if "qualificationReportDownloadUrl" in data:
        out["qualification_report_download_url"] = data[
            "qualificationReportDownloadUrl"
        ]
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCisScanReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.cis_report_format
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.report_target_accounts


class GetCisScanReportRequest(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN.</p>"""
    target_accounts: NotRequired[
        "capo_inspector2.types.report_target_accounts.ReportTargetAccounts"
    ]
    """<p>The target accounts.</p>"""
    report_format: "capo_inspector2.types.cis_report_format.CisReportFormat"
    """<p> The format of the report. Valid values are <code>PDF</code> and <code>CSV</code>. If no value is specified, the report format defaults to <code>PDF</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCisScanReportRequest) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "target_accounts" in value:
        import capo_inspector2.types.report_target_accounts

        out["targetAccounts"] = (
            capo_inspector2.types.report_target_accounts.serialize_json(
                value["target_accounts"]
            )
        )
    import capo_inspector2.types.cis_report_format

    out["reportFormat"] = capo_inspector2.types.cis_report_format.serialize_json(
        value.get("report_format", "PDF")
    )
    return out


def deserialize_json(data: dict) -> GetCisScanReportRequest:
    out: GetCisScanReportRequest = {}  # type: ignore[typeddict-item]
    if "scanArn" in data:
        out["scan_arn"] = data["scanArn"]
    else:
        raise DeserializationError("GetCisScanReportRequest.scan_arn required")
    if "targetAccounts" in data:
        import capo_inspector2.types.report_target_accounts

        out["target_accounts"] = (
            capo_inspector2.types.report_target_accounts.deserialize_json(
                data["targetAccounts"]
            )
        )
    if "reportFormat" in data:
        import capo_inspector2.types.cis_report_format

        out["report_format"] = capo_inspector2.types.cis_report_format.deserialize_json(
            data["reportFormat"]
        )
    else:
        out["report_format"] = "PDF"
    return out

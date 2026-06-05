"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteImageUsageReportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_usage_report_id


class DeleteImageUsageReportRequest(TypedDict):
    report_id: NotRequired["aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteImageUsageReportRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "report_id" in value:
        pairs.append((f"{prefix}.ReportId", str(value["report_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteImageUsageReportRequest:
    out: DeleteImageUsageReportRequest = {}  # type: ignore[typeddict-item]
    child_report_id = el.find("ReportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

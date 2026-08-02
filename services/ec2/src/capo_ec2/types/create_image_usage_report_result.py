"""Generated from Smithy shape ``com.amazonaws.ec2#CreateImageUsageReportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_usage_report_id


class CreateImageUsageReportResult(TypedDict, closed=True):
    report_id: NotRequired["capo_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateImageUsageReportResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "report_id" in value:
        pairs.append((f"{key_prefix}ReportId", str(value["report_id"])))


def deserialize_ec2_query(el: Element) -> CreateImageUsageReportResult:
    out: CreateImageUsageReportResult = {}  # type: ignore[typeddict-item]
    child_report_id = el.find("ReportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    return out

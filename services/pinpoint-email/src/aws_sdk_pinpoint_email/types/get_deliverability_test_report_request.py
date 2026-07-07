"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDeliverabilityTestReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.report_id


class GetDeliverabilityTestReportRequest(TypedDict, closed=True):
    report_id: "aws_sdk_pinpoint_email.types.report_id.ReportId"
    """<p>A unique string that identifies the predictive inbox placement test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeliverabilityTestReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeliverabilityTestReportRequest:
    out: GetDeliverabilityTestReportRequest = {}  # type: ignore[typeddict-item]
    return out

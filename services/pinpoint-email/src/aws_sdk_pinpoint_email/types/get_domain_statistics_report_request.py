"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDomainStatisticsReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.identity
    import aws_sdk_pinpoint_email.types.timestamp


class GetDomainStatisticsReportRequest(TypedDict, closed=True):
    domain: "aws_sdk_pinpoint_email.types.identity.Identity"
    """<p>The domain that you want to obtain deliverability metrics for.</p>"""
    start_date: "aws_sdk_pinpoint_email.types.timestamp.Timestamp"
    """<p>The first day (in Unix time) that you want to obtain domain deliverability metrics for.</p>"""
    end_date: "aws_sdk_pinpoint_email.types.timestamp.Timestamp"
    """<p>The last day (in Unix time) that you want to obtain domain deliverability metrics for. The <code>EndDate</code> that you specify has to be less than or equal to 30 days after the <code>StartDate</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainStatisticsReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainStatisticsReportRequest:
    out: GetDomainStatisticsReportRequest = {}  # type: ignore[typeddict-item]
    return out

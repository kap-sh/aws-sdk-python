"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeTestSetDiscrepancyReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id


class DescribeTestSetDiscrepancyReportRequest(TypedDict, closed=True):
    test_set_discrepancy_report_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the test set discrepancy report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestSetDiscrepancyReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTestSetDiscrepancyReportRequest:
    out: DescribeTestSetDiscrepancyReportRequest = {}  # type: ignore[typeddict-item]
    return out

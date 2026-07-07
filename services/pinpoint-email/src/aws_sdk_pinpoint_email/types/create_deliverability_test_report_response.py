"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateDeliverabilityTestReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.deliverability_test_status
    import aws_sdk_pinpoint_email.types.report_id


class CreateDeliverabilityTestReportResponse(TypedDict, closed=True):
    report_id: "aws_sdk_pinpoint_email.types.report_id.ReportId"
    """<p>A unique string that identifies the predictive inbox placement test.</p>"""
    deliverability_test_status: "aws_sdk_pinpoint_email.types.deliverability_test_status.DeliverabilityTestStatus"
    """<p>The status of the predictive inbox placement test. If the status is <code>IN_PROGRESS</code>, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is <code>COMPLETE</code>, then the test is finished, and you can use the <code>GetDeliverabilityTestReport</code> to view the results of the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeliverabilityTestReportResponse) -> dict:
    out: dict = {}
    out["ReportId"] = value["report_id"]
    import aws_sdk_pinpoint_email.types.deliverability_test_status

    out["DeliverabilityTestStatus"] = (
        aws_sdk_pinpoint_email.types.deliverability_test_status.serialize_json(
            value["deliverability_test_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateDeliverabilityTestReportResponse:
    out: CreateDeliverabilityTestReportResponse = {}  # type: ignore[typeddict-item]
    if "ReportId" in data:
        out["report_id"] = data["ReportId"]
    else:
        raise DeserializationError(
            "CreateDeliverabilityTestReportResponse.report_id required"
        )
    if "DeliverabilityTestStatus" in data:
        import aws_sdk_pinpoint_email.types.deliverability_test_status

        out["deliverability_test_status"] = (
            aws_sdk_pinpoint_email.types.deliverability_test_status.deserialize_json(
                data["DeliverabilityTestStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDeliverabilityTestReportResponse.deliverability_test_status required"
        )
    return out

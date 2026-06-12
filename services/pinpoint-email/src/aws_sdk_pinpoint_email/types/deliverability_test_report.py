"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeliverabilityTestReport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.deliverability_test_status
    import aws_sdk_pinpoint_email.types.deliverability_test_subject
    import aws_sdk_pinpoint_email.types.email_address
    import aws_sdk_pinpoint_email.types.report_id
    import aws_sdk_pinpoint_email.types.report_name
    import aws_sdk_pinpoint_email.types.timestamp


class DeliverabilityTestReport(TypedDict):
    report_id: NotRequired["aws_sdk_pinpoint_email.types.report_id.ReportId"]
    """<p>A unique string that identifies the predictive inbox placement test.</p>"""
    report_name: NotRequired["aws_sdk_pinpoint_email.types.report_name.ReportName"]
    """<p>A name that helps you identify a predictive inbox placement test report.</p>"""
    subject: NotRequired[
        "aws_sdk_pinpoint_email.types.deliverability_test_subject.DeliverabilityTestSubject"
    ]
    """<p>The subject line for an email that you submitted in a predictive inbox placement test.</p>"""
    from_email_address: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address.EmailAddress"
    ]
    """<p>The sender address that you specified for the predictive inbox placement test.</p>"""
    create_date: NotRequired["aws_sdk_pinpoint_email.types.timestamp.Timestamp"]
    """<p>The date and time when the predictive inbox placement test was created, in Unix time format.</p>"""
    deliverability_test_status: NotRequired[
        "aws_sdk_pinpoint_email.types.deliverability_test_status.DeliverabilityTestStatus"
    ]
    """<p>The status of the predictive inbox placement test. If the status is <code>IN_PROGRESS</code>, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is <code>COMPLETE</code>, then the test is finished, and you can use the <code>GetDeliverabilityTestReport</code> to view the results of the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeliverabilityTestReport) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["ReportId"] = value["report_id"]
    if "report_name" in value:
        out["ReportName"] = value["report_name"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "create_date" in value:
        import aws_sdk_pinpoint_email.types.timestamp

        out["CreateDate"] = aws_sdk_pinpoint_email.types.timestamp.serialize_json(
            value["create_date"]
        )
    if "deliverability_test_status" in value:
        import aws_sdk_pinpoint_email.types.deliverability_test_status

        out["DeliverabilityTestStatus"] = (
            aws_sdk_pinpoint_email.types.deliverability_test_status.serialize_json(
                value["deliverability_test_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeliverabilityTestReport:
    out: DeliverabilityTestReport = {}  # type: ignore[typeddict-item]
    if "ReportId" in data:
        out["report_id"] = data["ReportId"]
    if "ReportName" in data:
        out["report_name"] = data["ReportName"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "FromEmailAddress" in data:
        out["from_email_address"] = data["FromEmailAddress"]
    if "CreateDate" in data:
        import aws_sdk_pinpoint_email.types.timestamp

        out["create_date"] = aws_sdk_pinpoint_email.types.timestamp.deserialize_json(
            data["CreateDate"]
        )
    if "DeliverabilityTestStatus" in data:
        import aws_sdk_pinpoint_email.types.deliverability_test_status

        out["deliverability_test_status"] = (
            aws_sdk_pinpoint_email.types.deliverability_test_status.deserialize_json(
                data["DeliverabilityTestStatus"]
            )
        )
    return out

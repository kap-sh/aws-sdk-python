"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListDeliverabilityTestReportsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.deliverability_test_reports
    import aws_sdk_pinpoint_email.types.next_token


class ListDeliverabilityTestReportsResponse(TypedDict):
    deliverability_test_reports: "aws_sdk_pinpoint_email.types.deliverability_test_reports.DeliverabilityTestReports"
    """<p>An object that contains a lists of predictive inbox placement tests that you've performed.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional predictive inbox placement tests to list. To view additional predictive inbox placement tests, issue another request to <code>ListDeliverabilityTestReports</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeliverabilityTestReportsResponse) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_email.types.deliverability_test_reports

    out["DeliverabilityTestReports"] = (
        aws_sdk_pinpoint_email.types.deliverability_test_reports.serialize_json(
            value["deliverability_test_reports"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeliverabilityTestReportsResponse:
    out: ListDeliverabilityTestReportsResponse = {}  # type: ignore[typeddict-item]
    if "DeliverabilityTestReports" in data:
        import aws_sdk_pinpoint_email.types.deliverability_test_reports

        out["deliverability_test_reports"] = (
            aws_sdk_pinpoint_email.types.deliverability_test_reports.deserialize_json(
                data["DeliverabilityTestReports"]
            )
        )
    else:
        raise DeserializationError(
            "ListDeliverabilityTestReportsResponse.deliverability_test_reports required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

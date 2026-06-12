"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeliverabilityTestReports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.deliverability_test_report

DeliverabilityTestReports: TypeAlias = list[
    "aws_sdk_pinpoint_email.types.deliverability_test_report.DeliverabilityTestReport"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliverabilityTestReports) -> list:
    import aws_sdk_pinpoint_email.types.deliverability_test_report

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_email.types.deliverability_test_report.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeliverabilityTestReports:
    import aws_sdk_pinpoint_email.types.deliverability_test_report

    out: DeliverabilityTestReports = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_email.types.deliverability_test_report.deserialize_json(
                item
            )
        )
    return out

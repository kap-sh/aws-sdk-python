"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeliverabilityTestReports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.deliverability_test_report

DeliverabilityTestReports: TypeAlias = list[
    "capo_pinpoint_email.types.deliverability_test_report.DeliverabilityTestReport"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliverabilityTestReports) -> list:
    import capo_pinpoint_email.types.deliverability_test_report

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_email.types.deliverability_test_report.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeliverabilityTestReports:
    import capo_pinpoint_email.types.deliverability_test_report

    out: DeliverabilityTestReports = []
    for item in data:
        out.append(
            capo_pinpoint_email.types.deliverability_test_report.deserialize_json(item)
        )
    return out

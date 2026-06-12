"""Generated from Smithy shape ``com.amazonaws.connect#GetEffectiveHoursOfOperationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format
    import aws_sdk_connect.types.instance_id


class GetEffectiveHoursOfOperationsRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: (
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    )
    """<p>The identifier for the hours of operation.</p>"""
    from_date: "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    """<p>The date from when the hours of operation are listed.</p>"""
    to_date: "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    """<p>The date until when the hours of operation are listed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEffectiveHoursOfOperationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEffectiveHoursOfOperationsRequest:
    out: GetEffectiveHoursOfOperationsRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#DescribeHoursOfOperationOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.hours_of_operation_override_id
    import capo_connect.types.instance_id


class DescribeHoursOfOperationOverrideRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation.</p>"""
    hours_of_operation_override_id: (
        "capo_connect.types.hours_of_operation_override_id.HoursOfOperationOverrideId"
    )
    """<p>The identifier for the hours of operation override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHoursOfOperationOverrideRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeHoursOfOperationOverrideRequest:
    out: DescribeHoursOfOperationOverrideRequest = {}  # type: ignore[typeddict-item]
    return out

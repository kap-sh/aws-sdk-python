"""Generated from Smithy shape ``com.amazonaws.connect#DescribeHoursOfOperationOverrideResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_override


class DescribeHoursOfOperationOverrideResponse(TypedDict, closed=True):
    hours_of_operation_override: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_override.HoursOfOperationOverride"
    ]
    """<p>Information about the hours of operations override. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHoursOfOperationOverrideResponse) -> dict:
    out: dict = {}
    if "hours_of_operation_override" in value:
        import aws_sdk_connect.types.hours_of_operation_override

        out["HoursOfOperationOverride"] = (
            aws_sdk_connect.types.hours_of_operation_override.serialize_json(
                value["hours_of_operation_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeHoursOfOperationOverrideResponse:
    out: DescribeHoursOfOperationOverrideResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperationOverride" in data:
        import aws_sdk_connect.types.hours_of_operation_override

        out["hours_of_operation_override"] = (
            aws_sdk_connect.types.hours_of_operation_override.deserialize_json(
                data["HoursOfOperationOverride"]
            )
        )
    return out

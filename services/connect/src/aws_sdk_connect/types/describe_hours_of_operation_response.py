"""Generated from Smithy shape ``com.amazonaws.connect#DescribeHoursOfOperationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation


class DescribeHoursOfOperationResponse(TypedDict):
    hours_of_operation: NotRequired[
        "aws_sdk_connect.types.hours_of_operation.HoursOfOperation"
    ]
    """<p>The hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHoursOfOperationResponse) -> dict:
    out: dict = {}
    if "hours_of_operation" in value:
        import aws_sdk_connect.types.hours_of_operation

        out["HoursOfOperation"] = (
            aws_sdk_connect.types.hours_of_operation.serialize_json(
                value["hours_of_operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeHoursOfOperationResponse:
    out: DescribeHoursOfOperationResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperation" in data:
        import aws_sdk_connect.types.hours_of_operation

        out["hours_of_operation"] = (
            aws_sdk_connect.types.hours_of_operation.deserialize_json(
                data["HoursOfOperation"]
            )
        )
    return out

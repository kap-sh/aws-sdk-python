"""Generated from Smithy shape ``com.amazonaws.connect#DescribeHoursOfOperationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation


class DescribeHoursOfOperationResponse(TypedDict, closed=True):
    hours_of_operation: NotRequired[
        "capo_connect.types.hours_of_operation.HoursOfOperation"
    ]
    """<p>The hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHoursOfOperationResponse) -> dict:
    out: dict = {}
    if "hours_of_operation" in value:
        import capo_connect.types.hours_of_operation

        out["HoursOfOperation"] = capo_connect.types.hours_of_operation.serialize_json(
            value["hours_of_operation"]
        )
    return out


def deserialize_json(data: dict) -> DescribeHoursOfOperationResponse:
    out: DescribeHoursOfOperationResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperation" in data:
        import capo_connect.types.hours_of_operation

        out["hours_of_operation"] = (
            capo_connect.types.hours_of_operation.deserialize_json(
                data["HoursOfOperation"]
            )
        )
    return out

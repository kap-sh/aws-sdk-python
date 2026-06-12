"""Generated from Smithy shape ``com.amazonaws.connect#CreateHoursOfOperationOverrideResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_override_id


class CreateHoursOfOperationOverrideResponse(TypedDict):
    hours_of_operation_override_id: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_override_id.HoursOfOperationOverrideId"
    ]
    """<p>The identifier for the hours of operation override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHoursOfOperationOverrideResponse) -> dict:
    out: dict = {}
    if "hours_of_operation_override_id" in value:
        out["HoursOfOperationOverrideId"] = value["hours_of_operation_override_id"]
    return out


def deserialize_json(data: dict) -> CreateHoursOfOperationOverrideResponse:
    out: CreateHoursOfOperationOverrideResponse = {}  # type: ignore[typeddict-item]
    if "HoursOfOperationOverrideId" in data:
        out["hours_of_operation_override_id"] = data["HoursOfOperationOverrideId"]
    return out

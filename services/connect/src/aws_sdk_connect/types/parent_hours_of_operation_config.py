"""Generated from Smithy shape ``com.amazonaws.connect#ParentHoursOfOperationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_id


class ParentHoursOfOperationConfig(TypedDict, closed=True):
    hours_of_operation_id: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    ]
    """<p>The identifier for the hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentHoursOfOperationConfig) -> dict:
    out: dict = {}
    if "hours_of_operation_id" in value:
        out["HoursOfOperationId"] = value["hours_of_operation_id"]
    return out


def deserialize_json(data: dict) -> ParentHoursOfOperationConfig:
    out: ParentHoursOfOperationConfig = {}  # type: ignore[typeddict-item]
    if "HoursOfOperationId" in data:
        out["hours_of_operation_id"] = data["HoursOfOperationId"]
    return out

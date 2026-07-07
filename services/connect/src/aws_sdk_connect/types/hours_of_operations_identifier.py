"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationsIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.hours_of_operation_id


class HoursOfOperationsIdentifier(TypedDict, closed=True):
    name: "aws_sdk_connect.types.common_name_length127.CommonNameLength127"
    """<p>Name of the hours of operation</p>"""
    id: "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>Unique identifier of the hours of operation.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>Amazon Resource Name (ARN) of the hours of operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationsIdentifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> HoursOfOperationsIdentifier:
    out: HoursOfOperationsIdentifier = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("HoursOfOperationsIdentifier.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("HoursOfOperationsIdentifier.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.athena#DeleteCapacityReservationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.capacity_reservation_name


class DeleteCapacityReservationInput(TypedDict):
    name: "aws_sdk_athena.types.capacity_reservation_name.CapacityReservationName"
    """<p>The name of the capacity reservation to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCapacityReservationInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCapacityReservationInput:
    out: DeleteCapacityReservationInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteCapacityReservationInput.name required")
    return out

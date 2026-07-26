"""Generated from Smithy shape ``com.amazonaws.athena#CancelCapacityReservationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.capacity_reservation_name


class CancelCapacityReservationInput(TypedDict, closed=True):
    name: "capo_athena.types.capacity_reservation_name.CapacityReservationName"
    """<p>The name of the capacity reservation to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCapacityReservationInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCapacityReservationInput:
    out: CancelCapacityReservationInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CancelCapacityReservationInput.name required")
    return out

"""Generated from Smithy shape ``com.amazonaws.athena#UpdateCapacityReservationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.capacity_reservation_name
    import capo_athena.types.target_dpus_integer


class UpdateCapacityReservationInput(TypedDict, closed=True):
    target_dpus: "capo_athena.types.target_dpus_integer.TargetDpusInteger"
    """<p>The new number of requested data processing units.</p>"""
    name: "capo_athena.types.capacity_reservation_name.CapacityReservationName"
    """<p>The name of the capacity reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCapacityReservationInput) -> dict:
    out: dict = {}
    out["TargetDpus"] = value["target_dpus"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCapacityReservationInput:
    out: UpdateCapacityReservationInput = {}  # type: ignore[typeddict-item]
    if "TargetDpus" in data:
        out["target_dpus"] = data["TargetDpus"]
    else:
        raise DeserializationError(
            "UpdateCapacityReservationInput.target_dpus required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateCapacityReservationInput.name required")
    return out

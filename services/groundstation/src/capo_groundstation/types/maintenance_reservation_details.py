"""Generated from Smithy shape ``com.amazonaws.groundstation#MaintenanceReservationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.maintenance_type


class MaintenanceReservationDetails(TypedDict, closed=True):
    maintenance_type: "capo_groundstation.types.maintenance_type.MaintenanceType"
    """<p>Type of maintenance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceReservationDetails) -> dict:
    out: dict = {}
    import capo_groundstation.types.maintenance_type

    out["maintenanceType"] = capo_groundstation.types.maintenance_type.serialize_json(
        value["maintenance_type"]
    )
    return out


def deserialize_json(data: dict) -> MaintenanceReservationDetails:
    out: MaintenanceReservationDetails = {}  # type: ignore[typeddict-item]
    if "maintenanceType" in data:
        import capo_groundstation.types.maintenance_type

        out["maintenance_type"] = (
            capo_groundstation.types.maintenance_type.deserialize_json(
                data["maintenanceType"]
            )
        )
    else:
        raise DeserializationError(
            "MaintenanceReservationDetails.maintenance_type required"
        )
    return out

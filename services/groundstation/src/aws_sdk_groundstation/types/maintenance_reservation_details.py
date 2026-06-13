"""Generated from Smithy shape ``com.amazonaws.groundstation#MaintenanceReservationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.maintenance_type


class MaintenanceReservationDetails(TypedDict):
    maintenance_type: "aws_sdk_groundstation.types.maintenance_type.MaintenanceType"
    """<p>Type of maintenance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceReservationDetails) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.maintenance_type

    out["maintenanceType"] = (
        aws_sdk_groundstation.types.maintenance_type.serialize_json(
            value["maintenance_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> MaintenanceReservationDetails:
    out: MaintenanceReservationDetails = {}  # type: ignore[typeddict-item]
    if "maintenanceType" in data:
        import aws_sdk_groundstation.types.maintenance_type

        out["maintenance_type"] = (
            aws_sdk_groundstation.types.maintenance_type.deserialize_json(
                data["maintenanceType"]
            )
        )
    else:
        raise DeserializationError(
            "MaintenanceReservationDetails.maintenance_type required"
        )
    return out

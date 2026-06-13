"""Generated from Smithy shape ``com.amazonaws.groundstation#ReservationDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.contact_reservation_details
    import aws_sdk_groundstation.types.maintenance_reservation_details


class _ReservationDetails_maintenance(TypedDict):
    maintenance: "aws_sdk_groundstation.types.maintenance_reservation_details.MaintenanceReservationDetails"


class _ReservationDetails_contact(TypedDict):
    contact: "aws_sdk_groundstation.types.contact_reservation_details.ContactReservationDetails"


ReservationDetails: TypeAlias = (
    _ReservationDetails_maintenance | _ReservationDetails_contact
)


# --- restJson1 ser/de ---
def serialize_json(value: ReservationDetails) -> dict:
    if "maintenance" in value:
        import aws_sdk_groundstation.types.maintenance_reservation_details

        return {
            "maintenance": aws_sdk_groundstation.types.maintenance_reservation_details.serialize_json(
                value["maintenance"]
            )
        }
    elif "contact" in value:
        import aws_sdk_groundstation.types.contact_reservation_details

        return {
            "contact": aws_sdk_groundstation.types.contact_reservation_details.serialize_json(
                value["contact"]
            )
        }
    else:
        raise SerializationError("ReservationDetails: no variant present")


def deserialize_json(data: dict) -> ReservationDetails:
    if "maintenance" in data:
        import aws_sdk_groundstation.types.maintenance_reservation_details

        return {
            "maintenance": aws_sdk_groundstation.types.maintenance_reservation_details.deserialize_json(
                data["maintenance"]
            )
        }
    elif "contact" in data:
        import aws_sdk_groundstation.types.contact_reservation_details

        return {
            "contact": aws_sdk_groundstation.types.contact_reservation_details.deserialize_json(
                data["contact"]
            )
        }
    else:
        raise DeserializationError("ReservationDetails: no recognized variant key")

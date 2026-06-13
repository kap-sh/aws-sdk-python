"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.az_el_ephemeris_filter


class _EphemerisFilter_azEl(TypedDict):
    azEl: "aws_sdk_groundstation.types.az_el_ephemeris_filter.AzElEphemerisFilter"


EphemerisFilter: TypeAlias = _EphemerisFilter_azEl


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisFilter) -> dict:
    if "azEl" in value:
        import aws_sdk_groundstation.types.az_el_ephemeris_filter

        return {
            "azEl": aws_sdk_groundstation.types.az_el_ephemeris_filter.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisFilter: no variant present")


def deserialize_json(data: dict) -> EphemerisFilter:
    if "azEl" in data:
        import aws_sdk_groundstation.types.az_el_ephemeris_filter

        return {
            "azEl": aws_sdk_groundstation.types.az_el_ephemeris_filter.deserialize_json(
                data["azEl"]
            )
        }
    else:
        raise DeserializationError("EphemerisFilter: no recognized variant key")

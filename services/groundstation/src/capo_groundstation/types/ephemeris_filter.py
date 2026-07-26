"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_ephemeris_filter


class _EphemerisFilter_azEl(TypedDict, closed=True):
    azEl: "capo_groundstation.types.az_el_ephemeris_filter.AzElEphemerisFilter"


EphemerisFilter: TypeAlias = _EphemerisFilter_azEl


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisFilter) -> dict:
    if "azEl" in value:
        import capo_groundstation.types.az_el_ephemeris_filter

        return {
            "azEl": capo_groundstation.types.az_el_ephemeris_filter.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisFilter: no variant present")


def deserialize_json(data: dict) -> EphemerisFilter:
    if "azEl" in data:
        import capo_groundstation.types.az_el_ephemeris_filter

        return {
            "azEl": capo_groundstation.types.az_el_ephemeris_filter.deserialize_json(
                data["azEl"]
            )
        }
    else:
        raise DeserializationError("EphemerisFilter: no recognized variant key")

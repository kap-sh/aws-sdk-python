"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisTypeDescription``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_description


class _EphemerisTypeDescription_tle(TypedDict, closed=True):
    tle: "capo_groundstation.types.ephemeris_description.EphemerisDescription"


class _EphemerisTypeDescription_oem(TypedDict, closed=True):
    oem: "capo_groundstation.types.ephemeris_description.EphemerisDescription"


class _EphemerisTypeDescription_azEl(TypedDict, closed=True):
    azEl: "capo_groundstation.types.ephemeris_description.EphemerisDescription"


EphemerisTypeDescription: TypeAlias = (
    _EphemerisTypeDescription_tle
    | _EphemerisTypeDescription_oem
    | _EphemerisTypeDescription_azEl
)


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisTypeDescription) -> dict:
    if "tle" in value:
        import capo_groundstation.types.ephemeris_description

        return {
            "tle": capo_groundstation.types.ephemeris_description.serialize_json(
                value["tle"]
            )
        }
    elif "oem" in value:
        import capo_groundstation.types.ephemeris_description

        return {
            "oem": capo_groundstation.types.ephemeris_description.serialize_json(
                value["oem"]
            )
        }
    elif "azEl" in value:
        import capo_groundstation.types.ephemeris_description

        return {
            "azEl": capo_groundstation.types.ephemeris_description.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisTypeDescription: no variant present")


def deserialize_json(data: dict) -> EphemerisTypeDescription:
    if "tle" in data:
        import capo_groundstation.types.ephemeris_description

        return {
            "tle": capo_groundstation.types.ephemeris_description.deserialize_json(
                data["tle"]
            )
        }
    elif "oem" in data:
        import capo_groundstation.types.ephemeris_description

        return {
            "oem": capo_groundstation.types.ephemeris_description.deserialize_json(
                data["oem"]
            )
        }
    elif "azEl" in data:
        import capo_groundstation.types.ephemeris_description

        return {
            "azEl": capo_groundstation.types.ephemeris_description.deserialize_json(
                data["azEl"]
            )
        }
    else:
        raise DeserializationError(
            "EphemerisTypeDescription: no recognized variant key"
        )

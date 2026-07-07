"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.az_el_ephemeris
    import aws_sdk_groundstation.types.oem_ephemeris
    import aws_sdk_groundstation.types.tle_ephemeris


class _EphemerisData_tle(TypedDict, closed=True):
    tle: "aws_sdk_groundstation.types.tle_ephemeris.TLEEphemeris"


class _EphemerisData_oem(TypedDict, closed=True):
    oem: "aws_sdk_groundstation.types.oem_ephemeris.OEMEphemeris"


class _EphemerisData_azEl(TypedDict, closed=True):
    azEl: "aws_sdk_groundstation.types.az_el_ephemeris.AzElEphemeris"


EphemerisData: TypeAlias = _EphemerisData_tle | _EphemerisData_oem | _EphemerisData_azEl


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisData) -> dict:
    if "tle" in value:
        import aws_sdk_groundstation.types.tle_ephemeris

        return {
            "tle": aws_sdk_groundstation.types.tle_ephemeris.serialize_json(
                value["tle"]
            )
        }
    elif "oem" in value:
        import aws_sdk_groundstation.types.oem_ephemeris

        return {
            "oem": aws_sdk_groundstation.types.oem_ephemeris.serialize_json(
                value["oem"]
            )
        }
    elif "azEl" in value:
        import aws_sdk_groundstation.types.az_el_ephemeris

        return {
            "azEl": aws_sdk_groundstation.types.az_el_ephemeris.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisData: no variant present")


def deserialize_json(data: dict) -> EphemerisData:
    if "tle" in data:
        import aws_sdk_groundstation.types.tle_ephemeris

        return {
            "tle": aws_sdk_groundstation.types.tle_ephemeris.deserialize_json(
                data["tle"]
            )
        }
    elif "oem" in data:
        import aws_sdk_groundstation.types.oem_ephemeris

        return {
            "oem": aws_sdk_groundstation.types.oem_ephemeris.deserialize_json(
                data["oem"]
            )
        }
    elif "azEl" in data:
        import aws_sdk_groundstation.types.az_el_ephemeris

        return {
            "azEl": aws_sdk_groundstation.types.az_el_ephemeris.deserialize_json(
                data["azEl"]
            )
        }
    else:
        raise DeserializationError("EphemerisData: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisTypeDescription``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ephemeris_description


class _EphemerisTypeDescription_tle(TypedDict):
    tle: "aws_sdk_groundstation.types.ephemeris_description.EphemerisDescription"


class _EphemerisTypeDescription_oem(TypedDict):
    oem: "aws_sdk_groundstation.types.ephemeris_description.EphemerisDescription"


class _EphemerisTypeDescription_azEl(TypedDict):
    azEl: "aws_sdk_groundstation.types.ephemeris_description.EphemerisDescription"


EphemerisTypeDescription: TypeAlias = (
    _EphemerisTypeDescription_tle
    | _EphemerisTypeDescription_oem
    | _EphemerisTypeDescription_azEl
)


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisTypeDescription) -> dict:
    if "tle" in value:
        import aws_sdk_groundstation.types.ephemeris_description

        return {
            "tle": aws_sdk_groundstation.types.ephemeris_description.serialize_json(
                value["tle"]
            )
        }
    elif "oem" in value:
        import aws_sdk_groundstation.types.ephemeris_description

        return {
            "oem": aws_sdk_groundstation.types.ephemeris_description.serialize_json(
                value["oem"]
            )
        }
    elif "azEl" in value:
        import aws_sdk_groundstation.types.ephemeris_description

        return {
            "azEl": aws_sdk_groundstation.types.ephemeris_description.serialize_json(
                value["azEl"]
            )
        }
    else:
        raise SerializationError("EphemerisTypeDescription: no variant present")


def deserialize_json(data: dict) -> EphemerisTypeDescription:
    if "tle" in data:
        import aws_sdk_groundstation.types.ephemeris_description

        return {
            "tle": aws_sdk_groundstation.types.ephemeris_description.deserialize_json(
                data["tle"]
            )
        }
    elif "oem" in data:
        import aws_sdk_groundstation.types.ephemeris_description

        return {
            "oem": aws_sdk_groundstation.types.ephemeris_description.deserialize_json(
                data["oem"]
            )
        }
    elif "azEl" in data:
        import aws_sdk_groundstation.types.ephemeris_description

        return {
            "azEl": aws_sdk_groundstation.types.ephemeris_description.deserialize_json(
                data["azEl"]
            )
        }
    else:
        raise DeserializationError(
            "EphemerisTypeDescription: no recognized variant key"
        )

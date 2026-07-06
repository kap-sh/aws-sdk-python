"""Generated from Smithy shape ``com.amazonaws.groundstation#ProgramTrackSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.az_el_program_track_settings
    import aws_sdk_groundstation.types.oem_program_track_settings
    import aws_sdk_groundstation.types.tle_program_track_settings


class _ProgramTrackSettings_azEl(TypedDict, closed=True):
    azEl: "aws_sdk_groundstation.types.az_el_program_track_settings.AzElProgramTrackSettings"


class _ProgramTrackSettings_oem(TypedDict, closed=True):
    oem: (
        "aws_sdk_groundstation.types.oem_program_track_settings.OemProgramTrackSettings"
    )


class _ProgramTrackSettings_tle(TypedDict, closed=True):
    tle: (
        "aws_sdk_groundstation.types.tle_program_track_settings.TleProgramTrackSettings"
    )


ProgramTrackSettings: TypeAlias = (
    _ProgramTrackSettings_azEl | _ProgramTrackSettings_oem | _ProgramTrackSettings_tle
)


# --- restJson1 ser/de ---
def serialize_json(value: ProgramTrackSettings) -> dict:
    if "azEl" in value:
        import aws_sdk_groundstation.types.az_el_program_track_settings

        return {
            "azEl": aws_sdk_groundstation.types.az_el_program_track_settings.serialize_json(
                value["azEl"]
            )
        }
    elif "oem" in value:
        import aws_sdk_groundstation.types.oem_program_track_settings

        return {
            "oem": aws_sdk_groundstation.types.oem_program_track_settings.serialize_json(
                value["oem"]
            )
        }
    elif "tle" in value:
        import aws_sdk_groundstation.types.tle_program_track_settings

        return {
            "tle": aws_sdk_groundstation.types.tle_program_track_settings.serialize_json(
                value["tle"]
            )
        }
    else:
        raise SerializationError("ProgramTrackSettings: no variant present")


def deserialize_json(data: dict) -> ProgramTrackSettings:
    if "azEl" in data:
        import aws_sdk_groundstation.types.az_el_program_track_settings

        return {
            "azEl": aws_sdk_groundstation.types.az_el_program_track_settings.deserialize_json(
                data["azEl"]
            )
        }
    elif "oem" in data:
        import aws_sdk_groundstation.types.oem_program_track_settings

        return {
            "oem": aws_sdk_groundstation.types.oem_program_track_settings.deserialize_json(
                data["oem"]
            )
        }
    elif "tle" in data:
        import aws_sdk_groundstation.types.tle_program_track_settings

        return {
            "tle": aws_sdk_groundstation.types.tle_program_track_settings.deserialize_json(
                data["tle"]
            )
        }
    else:
        raise DeserializationError("ProgramTrackSettings: no recognized variant key")

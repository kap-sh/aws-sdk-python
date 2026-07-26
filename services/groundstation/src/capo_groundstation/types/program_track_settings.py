"""Generated from Smithy shape ``com.amazonaws.groundstation#ProgramTrackSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_program_track_settings
    import capo_groundstation.types.oem_program_track_settings
    import capo_groundstation.types.tle_program_track_settings


class _ProgramTrackSettings_azEl(TypedDict, closed=True):
    azEl: (
        "capo_groundstation.types.az_el_program_track_settings.AzElProgramTrackSettings"
    )


class _ProgramTrackSettings_oem(TypedDict, closed=True):
    oem: "capo_groundstation.types.oem_program_track_settings.OemProgramTrackSettings"


class _ProgramTrackSettings_tle(TypedDict, closed=True):
    tle: "capo_groundstation.types.tle_program_track_settings.TleProgramTrackSettings"


ProgramTrackSettings: TypeAlias = (
    _ProgramTrackSettings_azEl | _ProgramTrackSettings_oem | _ProgramTrackSettings_tle
)


# --- restJson1 ser/de ---
def serialize_json(value: ProgramTrackSettings) -> dict:
    if "azEl" in value:
        import capo_groundstation.types.az_el_program_track_settings

        return {
            "azEl": capo_groundstation.types.az_el_program_track_settings.serialize_json(
                value["azEl"]
            )
        }
    elif "oem" in value:
        import capo_groundstation.types.oem_program_track_settings

        return {
            "oem": capo_groundstation.types.oem_program_track_settings.serialize_json(
                value["oem"]
            )
        }
    elif "tle" in value:
        import capo_groundstation.types.tle_program_track_settings

        return {
            "tle": capo_groundstation.types.tle_program_track_settings.serialize_json(
                value["tle"]
            )
        }
    else:
        raise SerializationError("ProgramTrackSettings: no variant present")


def deserialize_json(data: dict) -> ProgramTrackSettings:
    if "azEl" in data:
        import capo_groundstation.types.az_el_program_track_settings

        return {
            "azEl": capo_groundstation.types.az_el_program_track_settings.deserialize_json(
                data["azEl"]
            )
        }
    elif "oem" in data:
        import capo_groundstation.types.oem_program_track_settings

        return {
            "oem": capo_groundstation.types.oem_program_track_settings.deserialize_json(
                data["oem"]
            )
        }
    elif "tle" in data:
        import capo_groundstation.types.tle_program_track_settings

        return {
            "tle": capo_groundstation.types.tle_program_track_settings.deserialize_json(
                data["tle"]
            )
        }
    else:
        raise DeserializationError("ProgramTrackSettings: no recognized variant key")

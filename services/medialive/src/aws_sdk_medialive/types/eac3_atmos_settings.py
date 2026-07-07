"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3AtmosSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double
    import aws_sdk_medialive.types.__integer_min1_max31
    import aws_sdk_medialive.types.eac3_atmos_coding_mode
    import aws_sdk_medialive.types.eac3_atmos_drc_line
    import aws_sdk_medialive.types.eac3_atmos_drc_rf


class Eac3AtmosSettings(TypedDict, closed=True):
    bitrate: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Average bitrate in bits/second. Valid bitrates depend on the coding mode."""
    coding_mode: NotRequired[
        "aws_sdk_medialive.types.eac3_atmos_coding_mode.Eac3AtmosCodingMode"
    ]
    """Dolby Digital Plus with Dolby Atmos coding mode. Determines number of channels."""
    dialnorm: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max31.__integerMin1Max31"
    ]
    """Sets the dialnorm for the output. Default 23."""
    drc_line: NotRequired[
        "aws_sdk_medialive.types.eac3_atmos_drc_line.Eac3AtmosDrcLine"
    ]
    """Sets the Dolby dynamic range compression profile."""
    drc_rf: NotRequired["aws_sdk_medialive.types.eac3_atmos_drc_rf.Eac3AtmosDrcRf"]
    """Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels."""
    height_trim: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Height dimensional trim. Sets the maximum amount to attenuate the height channels when the downstream player isn??t configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels."""
    surround_trim: NotRequired["aws_sdk_medialive.types.__double.__double"]
    """Surround dimensional trim. Sets the maximum amount to attenuate the surround channels when the downstream player isn't configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels."""


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosSettings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "coding_mode" in value:
        import aws_sdk_medialive.types.eac3_atmos_coding_mode

        out["codingMode"] = (
            aws_sdk_medialive.types.eac3_atmos_coding_mode.serialize_json(
                value["coding_mode"]
            )
        )
    if "dialnorm" in value:
        out["dialnorm"] = value["dialnorm"]
    if "drc_line" in value:
        import aws_sdk_medialive.types.eac3_atmos_drc_line

        out["drcLine"] = aws_sdk_medialive.types.eac3_atmos_drc_line.serialize_json(
            value["drc_line"]
        )
    if "drc_rf" in value:
        import aws_sdk_medialive.types.eac3_atmos_drc_rf

        out["drcRf"] = aws_sdk_medialive.types.eac3_atmos_drc_rf.serialize_json(
            value["drc_rf"]
        )
    if "height_trim" in value:
        out["heightTrim"] = value["height_trim"]
    if "surround_trim" in value:
        out["surroundTrim"] = value["surround_trim"]
    return out


def deserialize_json(data: dict) -> Eac3AtmosSettings:
    out: Eac3AtmosSettings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "codingMode" in data:
        import aws_sdk_medialive.types.eac3_atmos_coding_mode

        out["coding_mode"] = (
            aws_sdk_medialive.types.eac3_atmos_coding_mode.deserialize_json(
                data["codingMode"]
            )
        )
    if "dialnorm" in data:
        out["dialnorm"] = data["dialnorm"]
    if "drcLine" in data:
        import aws_sdk_medialive.types.eac3_atmos_drc_line

        out["drc_line"] = aws_sdk_medialive.types.eac3_atmos_drc_line.deserialize_json(
            data["drcLine"]
        )
    if "drcRf" in data:
        import aws_sdk_medialive.types.eac3_atmos_drc_rf

        out["drc_rf"] = aws_sdk_medialive.types.eac3_atmos_drc_rf.deserialize_json(
            data["drcRf"]
        )
    if "heightTrim" in data:
        out["height_trim"] = data["heightTrim"]
    if "surroundTrim" in data:
        out["surround_trim"] = data["surroundTrim"]
    return out

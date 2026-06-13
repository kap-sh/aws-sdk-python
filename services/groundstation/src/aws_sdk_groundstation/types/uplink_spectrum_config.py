"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkSpectrumConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.frequency
    import aws_sdk_groundstation.types.polarization


class UplinkSpectrumConfig(TypedDict):
    center_frequency: "aws_sdk_groundstation.types.frequency.Frequency"
    """<p>Center frequency of an uplink spectral <code>Config</code>. Valid values are between 2025 to 2120 MHz.</p>"""
    polarization: NotRequired["aws_sdk_groundstation.types.polarization.Polarization"]
    """<p>Polarization of an uplink spectral <code>Config</code>. Capturing both <code>\"RIGHT_HAND\"</code> and <code>\"LEFT_HAND\"</code> polarization requires two separate configs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UplinkSpectrumConfig) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.frequency

    out["centerFrequency"] = aws_sdk_groundstation.types.frequency.serialize_json(
        value["center_frequency"]
    )
    if "polarization" in value:
        import aws_sdk_groundstation.types.polarization

        out["polarization"] = aws_sdk_groundstation.types.polarization.serialize_json(
            value["polarization"]
        )
    return out


def deserialize_json(data: dict) -> UplinkSpectrumConfig:
    out: UplinkSpectrumConfig = {}  # type: ignore[typeddict-item]
    if "centerFrequency" in data:
        import aws_sdk_groundstation.types.frequency

        out["center_frequency"] = (
            aws_sdk_groundstation.types.frequency.deserialize_json(
                data["centerFrequency"]
            )
        )
    else:
        raise DeserializationError("UplinkSpectrumConfig.center_frequency required")
    if "polarization" in data:
        import aws_sdk_groundstation.types.polarization

        out["polarization"] = aws_sdk_groundstation.types.polarization.deserialize_json(
            data["polarization"]
        )
    return out

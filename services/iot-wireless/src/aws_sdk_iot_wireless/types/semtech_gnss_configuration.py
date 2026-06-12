"""Generated from Smithy shape ``com.amazonaws.iotwireless#SemtechGnssConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.position_configuration_fec
    import aws_sdk_iot_wireless.types.position_configuration_status


class SemtechGnssConfiguration(TypedDict):
    status: "aws_sdk_iot_wireless.types.position_configuration_status.PositionConfigurationStatus"
    """<p>The status indicating whether the solver is enabled.</p>"""
    fec: (
        "aws_sdk_iot_wireless.types.position_configuration_fec.PositionConfigurationFec"
    )
    """<p>Whether forward error correction is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemtechGnssConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.position_configuration_status

    out["Status"] = (
        aws_sdk_iot_wireless.types.position_configuration_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_iot_wireless.types.position_configuration_fec

    out["Fec"] = aws_sdk_iot_wireless.types.position_configuration_fec.serialize_json(
        value["fec"]
    )
    return out


def deserialize_json(data: dict) -> SemtechGnssConfiguration:
    out: SemtechGnssConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_iot_wireless.types.position_configuration_status

        out["status"] = (
            aws_sdk_iot_wireless.types.position_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("SemtechGnssConfiguration.status required")
    if "Fec" in data:
        import aws_sdk_iot_wireless.types.position_configuration_fec

        out["fec"] = (
            aws_sdk_iot_wireless.types.position_configuration_fec.deserialize_json(
                data["Fec"]
            )
        )
    else:
        raise DeserializationError("SemtechGnssConfiguration.fec required")
    return out

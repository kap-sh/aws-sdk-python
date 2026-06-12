"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.semtech_gnss_configuration


class PositionSolverConfigurations(TypedDict):
    semtech_gnss: NotRequired[
        "aws_sdk_iot_wireless.types.semtech_gnss_configuration.SemtechGnssConfiguration"
    ]
    """<p>The Semtech GNSS solver configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionSolverConfigurations) -> dict:
    out: dict = {}
    if "semtech_gnss" in value:
        import aws_sdk_iot_wireless.types.semtech_gnss_configuration

        out["SemtechGnss"] = (
            aws_sdk_iot_wireless.types.semtech_gnss_configuration.serialize_json(
                value["semtech_gnss"]
            )
        )
    return out


def deserialize_json(data: dict) -> PositionSolverConfigurations:
    out: PositionSolverConfigurations = {}  # type: ignore[typeddict-item]
    if "SemtechGnss" in data:
        import aws_sdk_iot_wireless.types.semtech_gnss_configuration

        out["semtech_gnss"] = (
            aws_sdk_iot_wireless.types.semtech_gnss_configuration.deserialize_json(
                data["SemtechGnss"]
            )
        )
    return out

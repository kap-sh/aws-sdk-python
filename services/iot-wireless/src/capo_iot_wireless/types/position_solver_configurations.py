"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.semtech_gnss_configuration


class PositionSolverConfigurations(TypedDict, closed=True):
    semtech_gnss: NotRequired[
        "capo_iot_wireless.types.semtech_gnss_configuration.SemtechGnssConfiguration"
    ]
    """<p>The Semtech GNSS solver configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionSolverConfigurations) -> dict:
    out: dict = {}
    if "semtech_gnss" in value:
        import capo_iot_wireless.types.semtech_gnss_configuration

        out["SemtechGnss"] = (
            capo_iot_wireless.types.semtech_gnss_configuration.serialize_json(
                value["semtech_gnss"]
            )
        )
    return out


def deserialize_json(data: dict) -> PositionSolverConfigurations:
    out: PositionSolverConfigurations = {}  # type: ignore[typeddict-item]
    if "SemtechGnss" in data:
        import capo_iot_wireless.types.semtech_gnss_configuration

        out["semtech_gnss"] = (
            capo_iot_wireless.types.semtech_gnss_configuration.deserialize_json(
                data["SemtechGnss"]
            )
        )
    return out

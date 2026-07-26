"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.semtech_gnss_detail


class PositionSolverDetails(TypedDict, closed=True):
    semtech_gnss: NotRequired[
        "capo_iot_wireless.types.semtech_gnss_detail.SemtechGnssDetail"
    ]
    """<p>The Semtech GNSS solver object details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionSolverDetails) -> dict:
    out: dict = {}
    if "semtech_gnss" in value:
        import capo_iot_wireless.types.semtech_gnss_detail

        out["SemtechGnss"] = capo_iot_wireless.types.semtech_gnss_detail.serialize_json(
            value["semtech_gnss"]
        )
    return out


def deserialize_json(data: dict) -> PositionSolverDetails:
    out: PositionSolverDetails = {}  # type: ignore[typeddict-item]
    if "SemtechGnss" in data:
        import capo_iot_wireless.types.semtech_gnss_detail

        out["semtech_gnss"] = (
            capo_iot_wireless.types.semtech_gnss_detail.deserialize_json(
                data["SemtechGnss"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.semtech_gnss_detail


class PositionSolverDetails(TypedDict):
    semtech_gnss: NotRequired[
        "aws_sdk_iot_wireless.types.semtech_gnss_detail.SemtechGnssDetail"
    ]
    """<p>The Semtech GNSS solver object details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PositionSolverDetails) -> dict:
    out: dict = {}
    if "semtech_gnss" in value:
        import aws_sdk_iot_wireless.types.semtech_gnss_detail

        out["SemtechGnss"] = (
            aws_sdk_iot_wireless.types.semtech_gnss_detail.serialize_json(
                value["semtech_gnss"]
            )
        )
    return out


def deserialize_json(data: dict) -> PositionSolverDetails:
    out: PositionSolverDetails = {}  # type: ignore[typeddict-item]
    if "SemtechGnss" in data:
        import aws_sdk_iot_wireless.types.semtech_gnss_detail

        out["semtech_gnss"] = (
            aws_sdk_iot_wireless.types.semtech_gnss_detail.deserialize_json(
                data["SemtechGnss"]
            )
        )
    return out

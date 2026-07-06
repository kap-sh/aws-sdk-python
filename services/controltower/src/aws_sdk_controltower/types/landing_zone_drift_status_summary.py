"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneDriftStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_drift_status


class LandingZoneDriftStatusSummary(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_controltower.types.landing_zone_drift_status.LandingZoneDriftStatus"
    ]
    """<p>The drift status of the landing zone. </p> <p>Valid values:</p> <ul> <li> <p> <code>DRIFTED</code>: The landing zone deployed in this configuration does not match the configuration that Amazon Web Services Control Tower expected. </p> </li> <li> <p> <code>IN_SYNC</code>: The landing zone deployed in this configuration matches the configuration that Amazon Web Services Control Tower expected. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneDriftStatusSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_controltower.types.landing_zone_drift_status

        out["status"] = (
            aws_sdk_controltower.types.landing_zone_drift_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> LandingZoneDriftStatusSummary:
    out: LandingZoneDriftStatusSummary = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_controltower.types.landing_zone_drift_status

        out["status"] = (
            aws_sdk_controltower.types.landing_zone_drift_status.deserialize_json(
                data["status"]
            )
        )
    return out

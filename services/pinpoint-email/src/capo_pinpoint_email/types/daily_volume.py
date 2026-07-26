"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DailyVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.domain_isp_placements
    import capo_pinpoint_email.types.timestamp
    import capo_pinpoint_email.types.volume_statistics


class DailyVolume(TypedDict, closed=True):
    start_date: NotRequired["capo_pinpoint_email.types.timestamp.Timestamp"]
    """<p>The date that the DailyVolume metrics apply to, in Unix time.</p>"""
    volume_statistics: NotRequired[
        "capo_pinpoint_email.types.volume_statistics.VolumeStatistics"
    ]
    """<p>An object that contains inbox placement metrics for a specific day in the analysis period.</p>"""
    domain_isp_placements: NotRequired[
        "capo_pinpoint_email.types.domain_isp_placements.DomainIspPlacements"
    ]
    """<p>An object that contains inbox placement metrics for a specified day in the analysis period, broken out by the recipient's email provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DailyVolume) -> dict:
    out: dict = {}
    if "start_date" in value:
        import capo_pinpoint_email.types.timestamp

        out["StartDate"] = capo_pinpoint_email.types.timestamp.serialize_json(
            value["start_date"]
        )
    if "volume_statistics" in value:
        import capo_pinpoint_email.types.volume_statistics

        out["VolumeStatistics"] = (
            capo_pinpoint_email.types.volume_statistics.serialize_json(
                value["volume_statistics"]
            )
        )
    if "domain_isp_placements" in value:
        import capo_pinpoint_email.types.domain_isp_placements

        out["DomainIspPlacements"] = (
            capo_pinpoint_email.types.domain_isp_placements.serialize_json(
                value["domain_isp_placements"]
            )
        )
    return out


def deserialize_json(data: dict) -> DailyVolume:
    out: DailyVolume = {}  # type: ignore[typeddict-item]
    if "StartDate" in data:
        import capo_pinpoint_email.types.timestamp

        out["start_date"] = capo_pinpoint_email.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    if "VolumeStatistics" in data:
        import capo_pinpoint_email.types.volume_statistics

        out["volume_statistics"] = (
            capo_pinpoint_email.types.volume_statistics.deserialize_json(
                data["VolumeStatistics"]
            )
        )
    if "DomainIspPlacements" in data:
        import capo_pinpoint_email.types.domain_isp_placements

        out["domain_isp_placements"] = (
            capo_pinpoint_email.types.domain_isp_placements.deserialize_json(
                data["DomainIspPlacements"]
            )
        )
    return out

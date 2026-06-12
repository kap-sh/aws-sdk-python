"""Generated from Smithy shape ``com.amazonaws.sesv2#OverallVolume``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.domain_isp_placements
    import aws_sdk_sesv2.types.percentage
    import aws_sdk_sesv2.types.volume_statistics


class OverallVolume(TypedDict):
    volume_statistics: NotRequired[
        "aws_sdk_sesv2.types.volume_statistics.VolumeStatistics"
    ]
    """<p>An object that contains information about the numbers of messages that arrived in recipients' inboxes and junk mail folders.</p>"""
    read_rate_percent: NotRequired["aws_sdk_sesv2.types.percentage.Percentage"]
    """<p>The percentage of emails that were sent from the domain that were read by their recipients.</p>"""
    domain_isp_placements: NotRequired[
        "aws_sdk_sesv2.types.domain_isp_placements.DomainIspPlacements"
    ]
    """<p>An object that contains inbox and junk mail placement metrics for individual email providers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverallVolume) -> dict:
    out: dict = {}
    if "volume_statistics" in value:
        import aws_sdk_sesv2.types.volume_statistics

        out["VolumeStatistics"] = aws_sdk_sesv2.types.volume_statistics.serialize_json(
            value["volume_statistics"]
        )
    if "read_rate_percent" in value:
        out["ReadRatePercent"] = value["read_rate_percent"]
    if "domain_isp_placements" in value:
        import aws_sdk_sesv2.types.domain_isp_placements

        out["DomainIspPlacements"] = (
            aws_sdk_sesv2.types.domain_isp_placements.serialize_json(
                value["domain_isp_placements"]
            )
        )
    return out


def deserialize_json(data: dict) -> OverallVolume:
    out: OverallVolume = {}  # type: ignore[typeddict-item]
    if "VolumeStatistics" in data:
        import aws_sdk_sesv2.types.volume_statistics

        out["volume_statistics"] = (
            aws_sdk_sesv2.types.volume_statistics.deserialize_json(
                data["VolumeStatistics"]
            )
        )
    if "ReadRatePercent" in data:
        out["read_rate_percent"] = data["ReadRatePercent"]
    if "DomainIspPlacements" in data:
        import aws_sdk_sesv2.types.domain_isp_placements

        out["domain_isp_placements"] = (
            aws_sdk_sesv2.types.domain_isp_placements.deserialize_json(
                data["DomainIspPlacements"]
            )
        )
    return out

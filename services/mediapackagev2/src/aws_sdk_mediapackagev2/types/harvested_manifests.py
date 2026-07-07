"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedManifests``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.harvested_dash_manifests_list
    import aws_sdk_mediapackagev2.types.harvested_hls_manifests_list
    import aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifests_list


class HarvestedManifests(TypedDict, closed=True):
    hls_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.harvested_hls_manifests_list.HarvestedHlsManifestsList"
    ]
    """<p>A list of harvested HLS manifests.</p>"""
    dash_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.harvested_dash_manifests_list.HarvestedDashManifestsList"
    ]
    """<p>A list of harvested DASH manifests.</p>"""
    low_latency_hls_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifests_list.HarvestedLowLatencyHlsManifestsList"
    ]
    """<p>A list of harvested Low-Latency HLS manifests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedManifests) -> dict:
    out: dict = {}
    if "hls_manifests" in value:
        import aws_sdk_mediapackagev2.types.harvested_hls_manifests_list

        out["HlsManifests"] = (
            aws_sdk_mediapackagev2.types.harvested_hls_manifests_list.serialize_json(
                value["hls_manifests"]
            )
        )
    if "dash_manifests" in value:
        import aws_sdk_mediapackagev2.types.harvested_dash_manifests_list

        out["DashManifests"] = (
            aws_sdk_mediapackagev2.types.harvested_dash_manifests_list.serialize_json(
                value["dash_manifests"]
            )
        )
    if "low_latency_hls_manifests" in value:
        import aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifests_list

        out["LowLatencyHlsManifests"] = (
            aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifests_list.serialize_json(
                value["low_latency_hls_manifests"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarvestedManifests:
    out: HarvestedManifests = {}  # type: ignore[typeddict-item]
    if "HlsManifests" in data:
        import aws_sdk_mediapackagev2.types.harvested_hls_manifests_list

        out["hls_manifests"] = (
            aws_sdk_mediapackagev2.types.harvested_hls_manifests_list.deserialize_json(
                data["HlsManifests"]
            )
        )
    if "DashManifests" in data:
        import aws_sdk_mediapackagev2.types.harvested_dash_manifests_list

        out["dash_manifests"] = (
            aws_sdk_mediapackagev2.types.harvested_dash_manifests_list.deserialize_json(
                data["DashManifests"]
            )
        )
    if "LowLatencyHlsManifests" in data:
        import aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifests_list

        out["low_latency_hls_manifests"] = (
            aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifests_list.deserialize_json(
                data["LowLatencyHlsManifests"]
            )
        )
    return out

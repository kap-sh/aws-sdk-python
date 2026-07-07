"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ScteDash``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.ad_marker_dash
    import aws_sdk_mediapackagev2.types.scte_in_manifests


class ScteDash(TypedDict, closed=True):
    ad_marker_dash: NotRequired[
        "aws_sdk_mediapackagev2.types.ad_marker_dash.AdMarkerDash"
    ]
    """<p>Choose how ad markers are included in the packaged content. If you include ad markers in the content stream in your upstream encoders, then you need to inform MediaPackage what to do with the ad markers in the output.</p> <p>Value description:</p> <ul> <li> <p> <code>Binary</code> - The SCTE-35 marker is expressed as a hex-string (Base64 string) rather than full XML.</p> </li> <li> <p> <code>XML</code> - The SCTE marker is expressed fully in XML.</p> </li> </ul>"""
    scte_in_manifests: NotRequired[
        "aws_sdk_mediapackagev2.types.scte_in_manifests.ScteInManifests"
    ]
    """<p>Controls which SCTE-35 events appear in DASH manifests. <code>ALL</code> includes all non-implicit SCTE-35 events. <code>MATCHES_FILTER</code> includes only events whose type matches the configured <code>ScteFilter</code>.</p> <p>If you don't specify a value, the default is <code>ALL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScteDash) -> dict:
    out: dict = {}
    if "ad_marker_dash" in value:
        import aws_sdk_mediapackagev2.types.ad_marker_dash

        out["AdMarkerDash"] = (
            aws_sdk_mediapackagev2.types.ad_marker_dash.serialize_json(
                value["ad_marker_dash"]
            )
        )
    if "scte_in_manifests" in value:
        import aws_sdk_mediapackagev2.types.scte_in_manifests

        out["ScteInManifests"] = (
            aws_sdk_mediapackagev2.types.scte_in_manifests.serialize_json(
                value["scte_in_manifests"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScteDash:
    out: ScteDash = {}  # type: ignore[typeddict-item]
    if "AdMarkerDash" in data:
        import aws_sdk_mediapackagev2.types.ad_marker_dash

        out["ad_marker_dash"] = (
            aws_sdk_mediapackagev2.types.ad_marker_dash.deserialize_json(
                data["AdMarkerDash"]
            )
        )
    if "ScteInManifests" in data:
        import aws_sdk_mediapackagev2.types.scte_in_manifests

        out["scte_in_manifests"] = (
            aws_sdk_mediapackagev2.types.scte_in_manifests.deserialize_json(
                data["ScteInManifests"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mediatailor#ManifestProcessingRules``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.ad_marker_passthrough


class ManifestProcessingRules(TypedDict):
    ad_marker_passthrough: NotRequired[
        "aws_sdk_mediatailor.types.ad_marker_passthrough.AdMarkerPassthrough"
    ]
    """<p>For HLS, when set to <code>true</code>, MediaTailor passes through <code>EXT-X-CUE-IN</code>, <code>EXT-X-CUE-OUT</code>, and <code>EXT-X-SPLICEPOINT-SCTE35</code> ad markers from the origin manifest to the MediaTailor personalized manifest.</p> <p>No logic is applied to these ad markers. For example, if <code>EXT-X-CUE-OUT</code> has a value of <code>60</code>, but no ads are filled for that ad break, MediaTailor will not set the value to <code>0</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManifestProcessingRules) -> dict:
    out: dict = {}
    if "ad_marker_passthrough" in value:
        import aws_sdk_mediatailor.types.ad_marker_passthrough

        out["AdMarkerPassthrough"] = (
            aws_sdk_mediatailor.types.ad_marker_passthrough.serialize_json(
                value["ad_marker_passthrough"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManifestProcessingRules:
    out: ManifestProcessingRules = {}  # type: ignore[typeddict-item]
    if "AdMarkerPassthrough" in data:
        import aws_sdk_mediatailor.types.ad_marker_passthrough

        out["ad_marker_passthrough"] = (
            aws_sdk_mediatailor.types.ad_marker_passthrough.deserialize_json(
                data["AdMarkerPassthrough"]
            )
        )
    return out

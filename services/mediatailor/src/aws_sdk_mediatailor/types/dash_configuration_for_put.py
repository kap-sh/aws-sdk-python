"""Generated from Smithy shape ``com.amazonaws.mediatailor#DashConfigurationForPut``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.origin_manifest_type


class DashConfigurationForPut(TypedDict):
    mpd_location: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that don't support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are <code>DISABLED</code> and <code>EMT_DEFAULT</code>. The <code>EMT_DEFAULT</code> setting enables the inclusion of the tag and is the default value.</p>"""
    origin_manifest_type: NotRequired[
        "aws_sdk_mediatailor.types.origin_manifest_type.OriginManifestType"
    ]
    """<p>The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to <code>SINGLE_PERIOD</code>. The default setting is <code>MULTI_PERIOD</code>. For multi-period manifests, omit this setting or set it to <code>MULTI_PERIOD</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashConfigurationForPut) -> dict:
    out: dict = {}
    if "mpd_location" in value:
        out["MpdLocation"] = value["mpd_location"]
    if "origin_manifest_type" in value:
        import aws_sdk_mediatailor.types.origin_manifest_type

        out["OriginManifestType"] = (
            aws_sdk_mediatailor.types.origin_manifest_type.serialize_json(
                value["origin_manifest_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashConfigurationForPut:
    out: DashConfigurationForPut = {}  # type: ignore[typeddict-item]
    if "MpdLocation" in data:
        out["mpd_location"] = data["MpdLocation"]
    if "OriginManifestType" in data:
        import aws_sdk_mediatailor.types.origin_manifest_type

        out["origin_manifest_type"] = (
            aws_sdk_mediatailor.types.origin_manifest_type.deserialize_json(
                data["OriginManifestType"]
            )
        )
    return out

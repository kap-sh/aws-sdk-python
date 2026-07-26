"""Generated from Smithy shape ``com.amazonaws.mediatailor#HlsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class HlsConfiguration(TypedDict, closed=True):
    manifest_endpoint_prefix: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HlsConfiguration) -> dict:
    out: dict = {}
    if "manifest_endpoint_prefix" in value:
        out["ManifestEndpointPrefix"] = value["manifest_endpoint_prefix"]
    return out


def deserialize_json(data: dict) -> HlsConfiguration:
    out: HlsConfiguration = {}  # type: ignore[typeddict-item]
    if "ManifestEndpointPrefix" in data:
        out["manifest_endpoint_prefix"] = data["ManifestEndpointPrefix"]
    return out

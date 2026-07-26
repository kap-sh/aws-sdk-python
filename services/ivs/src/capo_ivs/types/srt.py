"""Generated from Smithy shape ``com.amazonaws.ivs#Srt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.srt_endpoint
    import capo_ivs.types.srt_passphrase


class Srt(TypedDict, closed=True):
    endpoint: NotRequired["capo_ivs.types.srt_endpoint.SrtEndpoint"]
    """<p>The endpoint to be used when streaming with IVS using the SRT protocol.</p>"""
    passphrase: NotRequired["capo_ivs.types.srt_passphrase.SrtPassphrase"]
    """<p>Auto-generated passphrase to enable encryption. This field is applicable only if the end user has <i>not</i> enabled the <code>insecureIngest</code> option for the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Srt) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "passphrase" in value:
        out["passphrase"] = value["passphrase"]
    return out


def deserialize_json(data: dict) -> Srt:
    out: Srt = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "passphrase" in data:
        out["passphrase"] = data["passphrase"]
    return out

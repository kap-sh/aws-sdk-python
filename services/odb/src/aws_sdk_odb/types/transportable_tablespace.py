"""Generated from Smithy shape ``com.amazonaws.odb#TransportableTablespace``."""

from typing_extensions import NotRequired, TypedDict


class TransportableTablespace(TypedDict, closed=True):
    tts_bundle_url: NotRequired["str"]
    """<p>The URL of the transportable tablespace bundle to use when creating the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransportableTablespace) -> dict:
    out: dict = {}
    if "tts_bundle_url" in value:
        out["ttsBundleUrl"] = value["tts_bundle_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransportableTablespace:
    out: TransportableTablespace = {}  # type: ignore[typeddict-item]
    if "ttsBundleUrl" in data:
        out["tts_bundle_url"] = data["ttsBundleUrl"]
    return out

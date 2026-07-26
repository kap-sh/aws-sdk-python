"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageDescriptorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.descriptor_content_type


class GetSolNetworkPackageDescriptorOutput(TypedDict, closed=True):
    content_type: NotRequired[
        "capo_tnb.types.descriptor_content_type.DescriptorContentType"
    ]
    """<p>Indicates the media type of the resource.</p>"""
    nsd: NotRequired["bytes"]
    """<p>Contents of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageDescriptorOutput) -> dict:
    out: dict = {}
    if "nsd" in value:
        import capo_tnb.types._prelude.blob

        out["nsd"] = capo_tnb.types._prelude.blob.serialize_json(value["nsd"])
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageDescriptorOutput:
    out: GetSolNetworkPackageDescriptorOutput = {}  # type: ignore[typeddict-item]
    if "nsd" in data:
        import capo_tnb.types._prelude.blob

        out["nsd"] = capo_tnb.types._prelude.blob.deserialize_json(data["nsd"])
    return out

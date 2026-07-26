"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.package_content_type


class GetSolNetworkPackageContentOutput(TypedDict, closed=True):
    content_type: NotRequired["capo_tnb.types.package_content_type.PackageContentType"]
    """<p>Indicates the media type of the resource.</p>"""
    nsd_content: NotRequired["bytes"]
    """<p>Content of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageContentOutput) -> dict:
    out: dict = {}
    if "nsd_content" in value:
        import capo_tnb.types._prelude.blob

        out["nsdContent"] = capo_tnb.types._prelude.blob.serialize_json(
            value["nsd_content"]
        )
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageContentOutput:
    out: GetSolNetworkPackageContentOutput = {}  # type: ignore[typeddict-item]
    if "nsdContent" in data:
        import capo_tnb.types._prelude.blob

        out["nsd_content"] = capo_tnb.types._prelude.blob.deserialize_json(
            data["nsdContent"]
        )
    return out

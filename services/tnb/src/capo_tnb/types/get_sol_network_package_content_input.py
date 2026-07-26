"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id
    import capo_tnb.types.package_content_type


class GetSolNetworkPackageContentInput(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    accept: "capo_tnb.types.package_content_type.PackageContentType"
    """<p>The format of the package you want to download from the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageContentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageContentInput:
    out: GetSolNetworkPackageContentInput = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageContentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.package_content_type
    import capo_tnb.types.vnf_pkg_id


class GetSolFunctionPackageContentInput(TypedDict, closed=True):
    vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""
    accept: "capo_tnb.types.package_content_type.PackageContentType"
    """<p>The format of the package that you want to download from the function packages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageContentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageContentInput:
    out: GetSolFunctionPackageContentInput = {}  # type: ignore[typeddict-item]
    return out

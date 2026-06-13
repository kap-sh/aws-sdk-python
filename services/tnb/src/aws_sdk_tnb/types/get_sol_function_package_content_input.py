"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageContentInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.package_content_type
    import aws_sdk_tnb.types.vnf_pkg_id


class GetSolFunctionPackageContentInput(TypedDict):
    vnf_pkg_id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""
    accept: "aws_sdk_tnb.types.package_content_type.PackageContentType"
    """<p>The format of the package that you want to download from the function packages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageContentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageContentInput:
    out: GetSolFunctionPackageContentInput = {}  # type: ignore[typeddict-item]
    return out

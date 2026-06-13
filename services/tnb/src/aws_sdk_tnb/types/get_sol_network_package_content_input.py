"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkPackageContentInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.nsd_info_id
    import aws_sdk_tnb.types.package_content_type


class GetSolNetworkPackageContentInput(TypedDict):
    nsd_info_id: "aws_sdk_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""
    accept: "aws_sdk_tnb.types.package_content_type.PackageContentType"
    """<p>The format of the package you want to download from the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkPackageContentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolNetworkPackageContentInput:
    out: GetSolNetworkPackageContentInput = {}  # type: ignore[typeddict-item]
    return out

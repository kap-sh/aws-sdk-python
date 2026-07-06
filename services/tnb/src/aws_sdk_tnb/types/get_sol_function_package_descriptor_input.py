"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageDescriptorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.descriptor_content_type
    import aws_sdk_tnb.types.vnf_pkg_id


class GetSolFunctionPackageDescriptorInput(TypedDict, closed=True):
    vnf_pkg_id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""
    accept: "aws_sdk_tnb.types.descriptor_content_type.DescriptorContentType"
    """<p>Indicates which content types, expressed as MIME types, the client is able to understand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageDescriptorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageDescriptorInput:
    out: GetSolFunctionPackageDescriptorInput = {}  # type: ignore[typeddict-item]
    return out

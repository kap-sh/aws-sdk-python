"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionPackageInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.vnf_pkg_id


class GetSolFunctionPackageInput(TypedDict):
    vnf_pkg_id: "aws_sdk_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionPackageInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolFunctionPackageInput:
    out: GetSolFunctionPackageInput = {}  # type: ignore[typeddict-item]
    return out

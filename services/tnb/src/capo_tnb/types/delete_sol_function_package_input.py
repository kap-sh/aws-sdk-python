"""Generated from Smithy shape ``com.amazonaws.tnb#DeleteSolFunctionPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.vnf_pkg_id


class DeleteSolFunctionPackageInput(TypedDict, closed=True):
    vnf_pkg_id: "capo_tnb.types.vnf_pkg_id.VnfPkgId"
    """<p>ID of the function package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSolFunctionPackageInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSolFunctionPackageInput:
    out: DeleteSolFunctionPackageInput = {}  # type: ignore[typeddict-item]
    return out

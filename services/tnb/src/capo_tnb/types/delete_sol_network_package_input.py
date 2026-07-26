"""Generated from Smithy shape ``com.amazonaws.tnb#DeleteSolNetworkPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.nsd_info_id


class DeleteSolNetworkPackageInput(TypedDict, closed=True):
    nsd_info_id: "capo_tnb.types.nsd_info_id.NsdInfoId"
    """<p>ID of the network service descriptor in the network package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSolNetworkPackageInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSolNetworkPackageInput:
    out: DeleteSolNetworkPackageInput = {}  # type: ignore[typeddict-item]
    return out

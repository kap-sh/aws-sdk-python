"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkOperationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.ns_lcm_op_occ_id


class GetSolNetworkOperationInput(TypedDict, closed=True):
    ns_lcm_op_occ_id: "capo_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"
    """<p>The identifier of the network operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkOperationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolNetworkOperationInput:
    out: GetSolNetworkOperationInput = {}  # type: ignore[typeddict-item]
    return out

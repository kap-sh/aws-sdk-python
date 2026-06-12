"""Generated from Smithy shape ``com.amazonaws.tnb#CancelSolNetworkOperationInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_lcm_op_occ_id

class CancelSolNetworkOperationInput(TypedDict):
    ns_lcm_op_occ_id: "aws_sdk_tnb.types.ns_lcm_op_occ_id.NsLcmOpOccId"
    """<p>The identifier of the network operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelSolNetworkOperationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSolNetworkOperationInput:
    out: CancelSolNetworkOperationInput = {}  # type: ignore[typeddict-item]
    return out
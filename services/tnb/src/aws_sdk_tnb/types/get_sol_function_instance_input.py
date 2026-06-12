"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_tnb.types.vnf_instance_id

class GetSolFunctionInstanceInput(TypedDict):
    vnf_instance_id: "aws_sdk_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>ID of the network function.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionInstanceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolFunctionInstanceInput:
    out: GetSolFunctionInstanceInput = {}  # type: ignore[typeddict-item]
    return out
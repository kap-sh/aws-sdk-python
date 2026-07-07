"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolFunctionInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.vnf_instance_id


class GetSolFunctionInstanceInput(TypedDict, closed=True):
    vnf_instance_id: "aws_sdk_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>ID of the network function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolFunctionInstanceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolFunctionInstanceInput:
    out: GetSolFunctionInstanceInput = {}  # type: ignore[typeddict-item]
    return out

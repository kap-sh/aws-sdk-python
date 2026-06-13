"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_instance_id


class GetSolNetworkInstanceInput(TypedDict):
    ns_instance_id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolNetworkInstanceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSolNetworkInstanceInput:
    out: GetSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    return out

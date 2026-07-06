"""Generated from Smithy shape ``com.amazonaws.tnb#DeleteSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_instance_id


class DeleteSolNetworkInstanceInput(TypedDict, closed=True):
    ns_instance_id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>Network instance ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSolNetworkInstanceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSolNetworkInstanceInput:
    out: DeleteSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    return out

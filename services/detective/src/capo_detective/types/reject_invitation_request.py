"""Generated from Smithy shape ``com.amazonaws.detective#RejectInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_detective.errors import DeserializationError

if TYPE_CHECKING:
    import capo_detective.types.graph_arn


class RejectInvitationRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to reject the invitation to.</p> <p>The member account's current member status in the behavior graph must be <code>INVITED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectInvitationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> RejectInvitationRequest:
    out: RejectInvitationRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("RejectInvitationRequest.graph_arn required")
    return out

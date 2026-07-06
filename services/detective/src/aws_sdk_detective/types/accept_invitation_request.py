"""Generated from Smithy shape ``com.amazonaws.detective#AcceptInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn


class AcceptInvitationRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph that the member account is accepting the invitation for.</p> <p>The member account status in the behavior graph must be <code>INVITED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptInvitationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> AcceptInvitationRequest:
    out: AcceptInvitationRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("AcceptInvitationRequest.graph_arn required")
    return out

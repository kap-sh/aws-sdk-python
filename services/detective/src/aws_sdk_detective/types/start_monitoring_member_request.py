"""Generated from Smithy shape ``com.amazonaws.detective#StartMonitoringMemberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id
    import aws_sdk_detective.types.graph_arn


class StartMonitoringMemberRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    account_id: "aws_sdk_detective.types.account_id.AccountId"
    """<p>The account ID of the member account to try to enable.</p> <p>The account must be an invited member account with a status of <code>ACCEPTED_BUT_DISABLED</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMonitoringMemberRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> StartMonitoringMemberRequest:
    out: StartMonitoringMemberRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("StartMonitoringMemberRequest.graph_arn required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("StartMonitoringMemberRequest.account_id required")
    return out

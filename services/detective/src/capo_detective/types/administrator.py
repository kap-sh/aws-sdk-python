"""Generated from Smithy shape ``com.amazonaws.detective#Administrator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id
    import capo_detective.types.graph_arn
    import capo_detective.types.timestamp


class Administrator(TypedDict, closed=True):
    account_id: NotRequired["capo_detective.types.account_id.AccountId"]
    """<p>The Amazon Web Services account identifier of the Detective administrator account for the organization.</p>"""
    graph_arn: NotRequired["capo_detective.types.graph_arn.GraphArn"]
    """<p>The ARN of the organization behavior graph.</p>"""
    delegation_time: NotRequired["capo_detective.types.timestamp.Timestamp"]
    """<p>The date and time when the Detective administrator account was enabled. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Administrator) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    if "delegation_time" in value:
        import capo_detective.types.timestamp

        out["DelegationTime"] = capo_detective.types.timestamp.serialize_json(
            value["delegation_time"]
        )
    return out


def deserialize_json(data: dict) -> Administrator:
    out: Administrator = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    if "DelegationTime" in data:
        import capo_detective.types.timestamp

        out["delegation_time"] = capo_detective.types.timestamp.deserialize_json(
            data["DelegationTime"]
        )
    return out

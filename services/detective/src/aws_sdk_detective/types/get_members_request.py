"""Generated from Smithy shape ``com.amazonaws.detective#GetMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id_list
    import aws_sdk_detective.types.graph_arn


class GetMembersRequest(TypedDict, closed=True):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph for which to request the member details.</p>"""
    account_ids: "aws_sdk_detective.types.account_id_list.AccountIdList"
    """<p>The list of Amazon Web Services account identifiers for the member account for which to return member details. You can request details for up to 50 member accounts at a time.</p> <p>You cannot use <code>GetMembers</code> to retrieve information about member accounts that were removed from the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembersRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    import aws_sdk_detective.types.account_id_list

    out["AccountIds"] = aws_sdk_detective.types.account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> GetMembersRequest:
    out: GetMembersRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("GetMembersRequest.graph_arn required")
    if "AccountIds" in data:
        import aws_sdk_detective.types.account_id_list

        out["account_ids"] = aws_sdk_detective.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    else:
        raise DeserializationError("GetMembersRequest.account_ids required")
    return out

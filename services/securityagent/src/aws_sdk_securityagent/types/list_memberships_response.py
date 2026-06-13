"""Generated from Smithy shape ``com.amazonaws.securityagent#ListMembershipsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.membership_summary_list
    import aws_sdk_securityagent.types.next_token


class ListMembershipsResponse(TypedDict):
    membership_summaries: (
        "aws_sdk_securityagent.types.membership_summary_list.MembershipSummaryList"
    )
    """<p>The list of membership summaries.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsResponse) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.membership_summary_list

    out["membershipSummaries"] = (
        aws_sdk_securityagent.types.membership_summary_list.serialize_json(
            value["membership_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembershipsResponse:
    out: ListMembershipsResponse = {}  # type: ignore[typeddict-item]
    if "membershipSummaries" in data:
        import aws_sdk_securityagent.types.membership_summary_list

        out["membership_summaries"] = (
            aws_sdk_securityagent.types.membership_summary_list.deserialize_json(
                data["membershipSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMembershipsResponse.membership_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

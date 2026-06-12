"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListMembersInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.is_owned
    import aws_sdk_managedblockchain.types.member_list_max_results
    import aws_sdk_managedblockchain.types.member_status
    import aws_sdk_managedblockchain.types.pagination_token
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.string


class ListMembersInput(TypedDict):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network for which to list members.</p>"""
    name: NotRequired["aws_sdk_managedblockchain.types.string.String"]
    """<p>The optional name of the member to list.</p>"""
    status: NotRequired["aws_sdk_managedblockchain.types.member_status.MemberStatus"]
    """<p>An optional status specifier. If provided, only members currently in this status are listed.</p>"""
    is_owned: NotRequired["aws_sdk_managedblockchain.types.is_owned.IsOwned"]
    """<p>An optional Boolean value. If provided, the request is limited either to members that the current Amazon Web Services account owns (<code>true</code>) or that other Amazon Web Services accountsn own (<code>false</code>). If omitted, all members are listed.</p>"""
    max_results: NotRequired[
        "aws_sdk_managedblockchain.types.member_list_max_results.MemberListMaxResults"
    ]
    """<p>The maximum number of members to return in the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMembersInput:
    out: ListMembersInput = {}  # type: ignore[typeddict-item]
    return out

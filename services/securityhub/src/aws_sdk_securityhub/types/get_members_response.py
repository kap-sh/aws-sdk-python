"""Generated from Smithy shape ``com.amazonaws.securityhub#GetMembersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.member_list
    import aws_sdk_securityhub.types.result_list


class GetMembersResponse(TypedDict):
    members: NotRequired["aws_sdk_securityhub.types.member_list.MemberList"]
    """<p>The list of details about the Security Hub CSPM member accounts.</p>"""
    unprocessed_accounts: NotRequired[
        "aws_sdk_securityhub.types.result_list.ResultList"
    ]
    """<p>The list of Amazon Web Services accounts that could not be processed. For each account, the list includes the account ID and the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembersResponse) -> dict:
    out: dict = {}
    if "members" in value:
        import aws_sdk_securityhub.types.member_list

        out["Members"] = aws_sdk_securityhub.types.member_list.serialize_json(
            value["members"]
        )
    if "unprocessed_accounts" in value:
        import aws_sdk_securityhub.types.result_list

        out["UnprocessedAccounts"] = (
            aws_sdk_securityhub.types.result_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMembersResponse:
    out: GetMembersResponse = {}  # type: ignore[typeddict-item]
    if "Members" in data:
        import aws_sdk_securityhub.types.member_list

        out["members"] = aws_sdk_securityhub.types.member_list.deserialize_json(
            data["Members"]
        )
    if "UnprocessedAccounts" in data:
        import aws_sdk_securityhub.types.result_list

        out["unprocessed_accounts"] = (
            aws_sdk_securityhub.types.result_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out

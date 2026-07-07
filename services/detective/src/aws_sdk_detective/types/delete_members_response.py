"""Generated from Smithy shape ``com.amazonaws.detective#DeleteMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id_list
    import aws_sdk_detective.types.unprocessed_account_list


class DeleteMembersResponse(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_detective.types.account_id_list.AccountIdList"]
    """<p>The list of Amazon Web Services account identifiers for the member accounts that Detective successfully removed from the behavior graph.</p>"""
    unprocessed_accounts: NotRequired[
        "aws_sdk_detective.types.unprocessed_account_list.UnprocessedAccountList"
    ]
    """<p>The list of member accounts that Detective was not able to remove from the behavior graph. For each member account, provides the reason that the deletion could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMembersResponse) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_detective.types.account_id_list

        out["AccountIds"] = aws_sdk_detective.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    if "unprocessed_accounts" in value:
        import aws_sdk_detective.types.unprocessed_account_list

        out["UnprocessedAccounts"] = (
            aws_sdk_detective.types.unprocessed_account_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteMembersResponse:
    out: DeleteMembersResponse = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_detective.types.account_id_list

        out["account_ids"] = aws_sdk_detective.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    if "UnprocessedAccounts" in data:
        import aws_sdk_detective.types.unprocessed_account_list

        out["unprocessed_accounts"] = (
            aws_sdk_detective.types.unprocessed_account_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out

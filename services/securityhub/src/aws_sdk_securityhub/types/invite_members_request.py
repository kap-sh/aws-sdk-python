"""Generated from Smithy shape ``com.amazonaws.securityhub#InviteMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.account_id_list


class InviteMembersRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_securityhub.types.account_id_list.AccountIdList"]
    """<p>The list of account IDs of the Amazon Web Services accounts to invite to Security Hub CSPM as members. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteMembersRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_securityhub.types.account_id_list

        out["AccountIds"] = aws_sdk_securityhub.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> InviteMembersRequest:
    out: InviteMembersRequest = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_securityhub.types.account_id_list

        out["account_ids"] = aws_sdk_securityhub.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    return out

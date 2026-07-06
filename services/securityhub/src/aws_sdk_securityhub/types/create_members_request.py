"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateMembersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.account_details_list


class CreateMembersRequest(TypedDict, closed=True):
    account_details: NotRequired[
        "aws_sdk_securityhub.types.account_details_list.AccountDetailsList"
    ]
    """<p>The list of accounts to associate with the Security Hub CSPM administrator account. For each account, the list includes the account ID and optionally the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersRequest) -> dict:
    out: dict = {}
    if "account_details" in value:
        import aws_sdk_securityhub.types.account_details_list

        out["AccountDetails"] = (
            aws_sdk_securityhub.types.account_details_list.serialize_json(
                value["account_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMembersRequest:
    out: CreateMembersRequest = {}  # type: ignore[typeddict-item]
    if "AccountDetails" in data:
        import aws_sdk_securityhub.types.account_details_list

        out["account_details"] = (
            aws_sdk_securityhub.types.account_details_list.deserialize_json(
                data["AccountDetails"]
            )
        )
    return out

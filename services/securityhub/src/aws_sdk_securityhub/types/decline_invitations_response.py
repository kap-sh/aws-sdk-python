"""Generated from Smithy shape ``com.amazonaws.securityhub#DeclineInvitationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.result_list


class DeclineInvitationsResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "aws_sdk_securityhub.types.result_list.ResultList"
    ]
    """<p>The list of Amazon Web Services accounts that were not processed. For each account, the list includes the account ID and the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeclineInvitationsResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import aws_sdk_securityhub.types.result_list

        out["UnprocessedAccounts"] = (
            aws_sdk_securityhub.types.result_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeclineInvitationsResponse:
    out: DeclineInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "UnprocessedAccounts" in data:
        import aws_sdk_securityhub.types.result_list

        out["unprocessed_accounts"] = (
            aws_sdk_securityhub.types.result_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out

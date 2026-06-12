"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateMembersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.result_list


class CreateMembersResponse(TypedDict):
    unprocessed_accounts: NotRequired[
        "aws_sdk_securityhub.types.result_list.ResultList"
    ]
    """<p>The list of Amazon Web Services accounts that were not processed. For each account, the list includes the account ID and the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import aws_sdk_securityhub.types.result_list

        out["UnprocessedAccounts"] = (
            aws_sdk_securityhub.types.result_list.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMembersResponse:
    out: CreateMembersResponse = {}  # type: ignore[typeddict-item]
    if "UnprocessedAccounts" in data:
        import aws_sdk_securityhub.types.result_list

        out["unprocessed_accounts"] = (
            aws_sdk_securityhub.types.result_list.deserialize_json(
                data["UnprocessedAccounts"]
            )
        )
    return out

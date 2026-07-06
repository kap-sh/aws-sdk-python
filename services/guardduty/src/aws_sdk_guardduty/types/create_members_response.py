"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.unprocessed_accounts


class CreateMembersResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "aws_sdk_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>A list of objects that include the <code>accountIds</code> of the unprocessed accounts and a result string that explains why each was unprocessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembersResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMembersResponse:
    out: CreateMembersResponse = {}  # type: ignore[typeddict-item]
    if "unprocessedAccounts" in data:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

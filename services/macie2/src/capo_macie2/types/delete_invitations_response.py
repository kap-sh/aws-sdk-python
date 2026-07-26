"""Generated from Smithy shape ``com.amazonaws.macie2#DeleteInvitationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_unprocessed_account


class DeleteInvitationsResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "capo_macie2.types.__list_of_unprocessed_account.__listOfUnprocessedAccount"
    ]
    """<p>An array of objects, one for each account whose invitation hasn't been deleted. Each object identifies the account and explains why the request hasn't been processed for that account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInvitationsResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import capo_macie2.types.__list_of_unprocessed_account

        out["unprocessedAccounts"] = (
            capo_macie2.types.__list_of_unprocessed_account.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteInvitationsResponse:
    out: DeleteInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "unprocessedAccounts" in data:
        import capo_macie2.types.__list_of_unprocessed_account

        out["unprocessed_accounts"] = (
            capo_macie2.types.__list_of_unprocessed_account.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

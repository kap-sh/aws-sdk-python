"""Generated from Smithy shape ``com.amazonaws.macie2#DeleteInvitationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string


class DeleteInvitationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists Amazon Web Services account IDs, one for each account that sent an invitation to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_macie2.types.__list_of__string

        out["accountIds"] = capo_macie2.types.__list_of__string.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DeleteInvitationsRequest:
    out: DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_macie2.types.__list_of__string

        out["account_ids"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["accountIds"]
        )
    return out

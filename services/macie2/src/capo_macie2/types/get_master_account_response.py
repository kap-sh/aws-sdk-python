"""Generated from Smithy shape ``com.amazonaws.macie2#GetMasterAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.invitation


class GetMasterAccountResponse(TypedDict, closed=True):
    master: NotRequired["capo_macie2.types.invitation.Invitation"]
    """<p>(Deprecated) The Amazon Web Services account ID for the administrator account. If the accounts are associated by a Macie membership invitation, this object also provides details about the invitation that was sent to establish the relationship between the accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMasterAccountResponse) -> dict:
    out: dict = {}
    if "master" in value:
        import capo_macie2.types.invitation

        out["master"] = capo_macie2.types.invitation.serialize_json(value["master"])
    return out


def deserialize_json(data: dict) -> GetMasterAccountResponse:
    out: GetMasterAccountResponse = {}  # type: ignore[typeddict-item]
    if "master" in data:
        import capo_macie2.types.invitation

        out["master"] = capo_macie2.types.invitation.deserialize_json(data["master"])
    return out

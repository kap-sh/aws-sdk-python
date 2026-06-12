"""Generated from Smithy shape ``com.amazonaws.macie2#GetMasterAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.invitation


class GetMasterAccountResponse(TypedDict):
    master: NotRequired["aws_sdk_macie2.types.invitation.Invitation"]
    """<p>(Deprecated) The Amazon Web Services account ID for the administrator account. If the accounts are associated by a Macie membership invitation, this object also provides details about the invitation that was sent to establish the relationship between the accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMasterAccountResponse) -> dict:
    out: dict = {}
    if "master" in value:
        import aws_sdk_macie2.types.invitation

        out["master"] = aws_sdk_macie2.types.invitation.serialize_json(value["master"])
    return out


def deserialize_json(data: dict) -> GetMasterAccountResponse:
    out: GetMasterAccountResponse = {}  # type: ignore[typeddict-item]
    if "master" in data:
        import aws_sdk_macie2.types.invitation

        out["master"] = aws_sdk_macie2.types.invitation.deserialize_json(data["master"])
    return out

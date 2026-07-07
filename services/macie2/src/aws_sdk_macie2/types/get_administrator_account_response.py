"""Generated from Smithy shape ``com.amazonaws.macie2#GetAdministratorAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.invitation


class GetAdministratorAccountResponse(TypedDict, closed=True):
    administrator: NotRequired["aws_sdk_macie2.types.invitation.Invitation"]
    """<p>The Amazon Web Services account ID for the administrator account. If the accounts are associated by an Amazon Macie membership invitation, this object also provides details about the invitation that was sent to establish the relationship between the accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdministratorAccountResponse) -> dict:
    out: dict = {}
    if "administrator" in value:
        import aws_sdk_macie2.types.invitation

        out["administrator"] = aws_sdk_macie2.types.invitation.serialize_json(
            value["administrator"]
        )
    return out


def deserialize_json(data: dict) -> GetAdministratorAccountResponse:
    out: GetAdministratorAccountResponse = {}  # type: ignore[typeddict-item]
    if "administrator" in data:
        import aws_sdk_macie2.types.invitation

        out["administrator"] = aws_sdk_macie2.types.invitation.deserialize_json(
            data["administrator"]
        )
    return out

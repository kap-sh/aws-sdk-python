"""Generated from Smithy shape ``com.amazonaws.macie2#DeclineInvitationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string


class DeclineInvitationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists Amazon Web Services account IDs, one for each account that sent an invitation to decline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeclineInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["accountIds"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DeclineInvitationsRequest:
    out: DeclineInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["account_ids"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["accountIds"]
        )
    return out

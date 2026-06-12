"""Generated from Smithy shape ``com.amazonaws.macie2#DeleteInvitationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of__string


class DeleteInvitationsRequest(TypedDict):
    account_ids: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists Amazon Web Services account IDs, one for each account that sent an invitation to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["accountIds"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DeleteInvitationsRequest:
    out: DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["account_ids"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["accountIds"]
        )
    return out

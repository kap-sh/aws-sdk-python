"""Generated from Smithy shape ``com.amazonaws.macie2#CreateInvitationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string


class CreateInvitationsRequest(TypedDict):
    account_ids: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists Amazon Web Services account IDs, one for each account to send the invitation to.</p>"""
    disable_email_notification: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether to send the invitation as an email message. If this value is false, Amazon Macie sends the invitation (as an email message) to the email address that you specified for the recipient's account when you associated the account with your account. The default value is false.</p>"""
    message: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>Custom text to include in the email message that contains the invitation. The text can contain as many as 80 alphanumeric characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["accountIds"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["account_ids"]
        )
    if "disable_email_notification" in value:
        out["disableEmailNotification"] = value["disable_email_notification"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateInvitationsRequest:
    out: CreateInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["account_ids"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["accountIds"]
        )
    if "disableEmailNotification" in data:
        out["disable_email_notification"] = data["disableEmailNotification"]
    if "message" in data:
        out["message"] = data["message"]
    return out

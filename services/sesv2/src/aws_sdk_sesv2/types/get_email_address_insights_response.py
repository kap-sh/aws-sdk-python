"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailAddressInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.mailbox_validation


class GetEmailAddressInsightsResponse(TypedDict, closed=True):
    mailbox_validation: NotRequired[
        "aws_sdk_sesv2.types.mailbox_validation.MailboxValidation"
    ]
    """<p>Detailed validation results for the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailAddressInsightsResponse) -> dict:
    out: dict = {}
    if "mailbox_validation" in value:
        import aws_sdk_sesv2.types.mailbox_validation

        out["MailboxValidation"] = (
            aws_sdk_sesv2.types.mailbox_validation.serialize_json(
                value["mailbox_validation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEmailAddressInsightsResponse:
    out: GetEmailAddressInsightsResponse = {}  # type: ignore[typeddict-item]
    if "MailboxValidation" in data:
        import aws_sdk_sesv2.types.mailbox_validation

        out["mailbox_validation"] = (
            aws_sdk_sesv2.types.mailbox_validation.deserialize_json(
                data["MailboxValidation"]
            )
        )
    return out

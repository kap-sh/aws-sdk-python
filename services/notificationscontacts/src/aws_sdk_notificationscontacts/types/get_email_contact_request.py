"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#GetEmailContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.email_contact_arn


class GetEmailContactRequest(TypedDict):
    arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The Amazon Resource Name (ARN) of the email contact to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEmailContactRequest:
    out: GetEmailContactRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#SendActivationCodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.email_contact_arn


class SendActivationCodeRequest(TypedDict):
    arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendActivationCodeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendActivationCodeRequest:
    out: SendActivationCodeRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#DeleteEmailContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact_arn


class DeleteEmailContactRequest(TypedDict, closed=True):
    arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailContactRequest:
    out: DeleteEmailContactRequest = {}  # type: ignore[typeddict-item]
    return out

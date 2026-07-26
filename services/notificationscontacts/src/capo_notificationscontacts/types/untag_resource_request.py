"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact_arn
    import capo_notificationscontacts.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.</p>"""
    tag_keys: "capo_notificationscontacts.types.tag_keys.TagKeys"
    """<p>Specifies a list of tag keys that you want to remove from the specified resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out

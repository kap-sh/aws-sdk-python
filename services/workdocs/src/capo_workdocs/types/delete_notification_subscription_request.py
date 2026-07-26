"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteNotificationSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type


class DeleteNotificationSubscriptionRequest(TypedDict, closed=True):
    subscription_id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the subscription.</p>"""
    organization_id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotificationSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotificationSubscriptionRequest:
    out: DeleteNotificationSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out

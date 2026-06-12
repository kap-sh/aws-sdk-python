"""Generated from Smithy shape ``com.amazonaws.workdocs#DeleteNotificationSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type


class DeleteNotificationSubscriptionRequest(TypedDict):
    subscription_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the subscription.</p>"""
    organization_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotificationSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotificationSubscriptionRequest:
    out: DeleteNotificationSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.datazone#RevokeSubscriptionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscription_id


class RevokeSubscriptionInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain where you want to revoke a subscription.</p>"""
    identifier: "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    """<p>The identifier of the revoked subscription.</p>"""
    retain_permissions: NotRequired["bool"]
    """<p>Specifies whether permissions are retained when the subscription is revoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeSubscriptionInput) -> dict:
    out: dict = {}
    if "retain_permissions" in value:
        out["retainPermissions"] = value["retain_permissions"]
    return out


def deserialize_json(data: dict) -> RevokeSubscriptionInput:
    out: RevokeSubscriptionInput = {}  # type: ignore[typeddict-item]
    if "retainPermissions" in data:
        out["retain_permissions"] = data["retainPermissions"]
    return out

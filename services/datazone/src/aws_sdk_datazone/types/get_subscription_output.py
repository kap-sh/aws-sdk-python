"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.subscribed_listing
    import aws_sdk_datazone.types.subscribed_principal
    import aws_sdk_datazone.types.subscription_id
    import aws_sdk_datazone.types.subscription_request_id
    import aws_sdk_datazone.types.subscription_status
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class GetSubscriptionOutput(TypedDict):
    id: "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    """<p>The ID of the subscription.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription exists.</p>"""
    status: "aws_sdk_datazone.types.subscription_status.SubscriptionStatus"
    """<p>The status of the subscription.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription was created.</p>"""
    updated_at: "aws_sdk_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription was updated.</p>"""
    subscribed_principal: (
        "aws_sdk_datazone.types.subscribed_principal.SubscribedPrincipal"
    )
    """<p>The principal that owns the subscription.</p>"""
    subscribed_listing: "aws_sdk_datazone.types.subscribed_listing.SubscribedListing"
    """<p>The details of the published asset for which the subscription grant is created.</p>"""
    subscription_request_id: NotRequired[
        "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    ]
    """<p>The ID of the subscription request.</p>"""
    retain_permissions: NotRequired["bool"]
    """<p>The retain permissions of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import aws_sdk_datazone.types.subscription_status

    out["status"] = aws_sdk_datazone.types.subscription_status.serialize_json(
        value["status"]
    )
    import aws_sdk_datazone.types.created_at

    out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import aws_sdk_datazone.types.updated_at

    out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    import aws_sdk_datazone.types.subscribed_principal

    out["subscribedPrincipal"] = (
        aws_sdk_datazone.types.subscribed_principal.serialize_json(
            value["subscribed_principal"]
        )
    )
    import aws_sdk_datazone.types.subscribed_listing

    out["subscribedListing"] = aws_sdk_datazone.types.subscribed_listing.serialize_json(
        value["subscribed_listing"]
    )
    if "subscription_request_id" in value:
        out["subscriptionRequestId"] = value["subscription_request_id"]
    if "retain_permissions" in value:
        out["retainPermissions"] = value["retain_permissions"]
    return out


def deserialize_json(data: dict) -> GetSubscriptionOutput:
    out: GetSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSubscriptionOutput.id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetSubscriptionOutput.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetSubscriptionOutput.domain_id required")
    if "status" in data:
        import aws_sdk_datazone.types.subscription_status

        out["status"] = aws_sdk_datazone.types.subscription_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetSubscriptionOutput.status required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSubscriptionOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetSubscriptionOutput.updated_at required")
    if "subscribedPrincipal" in data:
        import aws_sdk_datazone.types.subscribed_principal

        out["subscribed_principal"] = (
            aws_sdk_datazone.types.subscribed_principal.deserialize_json(
                data["subscribedPrincipal"]
            )
        )
    else:
        raise DeserializationError(
            "GetSubscriptionOutput.subscribed_principal required"
        )
    if "subscribedListing" in data:
        import aws_sdk_datazone.types.subscribed_listing

        out["subscribed_listing"] = (
            aws_sdk_datazone.types.subscribed_listing.deserialize_json(
                data["subscribedListing"]
            )
        )
    else:
        raise DeserializationError("GetSubscriptionOutput.subscribed_listing required")
    if "subscriptionRequestId" in data:
        out["subscription_request_id"] = data["subscriptionRequestId"]
    if "retainPermissions" in data:
        out["retain_permissions"] = data["retainPermissions"]
    return out

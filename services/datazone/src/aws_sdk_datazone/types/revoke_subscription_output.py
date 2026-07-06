"""Generated from Smithy shape ``com.amazonaws.datazone#RevokeSubscriptionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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


class RevokeSubscriptionOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    """<p>The identifier of the revoked subscription.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The identifier of the user who revoked the subscription.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who revoked the subscription.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain where you want to revoke a subscription.</p>"""
    status: "aws_sdk_datazone.types.subscription_status.SubscriptionStatus"
    """<p>The status of the revoked subscription.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription was revoked.</p>"""
    updated_at: "aws_sdk_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription was revoked.</p>"""
    subscribed_principal: (
        "aws_sdk_datazone.types.subscribed_principal.SubscribedPrincipal"
    )
    """<p>The subscribed principal of the revoked subscription.</p>"""
    subscribed_listing: "aws_sdk_datazone.types.subscribed_listing.SubscribedListing"
    """<p>The subscribed listing of the revoked subscription.</p>"""
    subscription_request_id: NotRequired[
        "aws_sdk_datazone.types.subscription_request_id.SubscriptionRequestId"
    ]
    """<p>The identifier of the subscription request for the revoked subscription.</p>"""
    retain_permissions: NotRequired["bool"]
    """<p>Specifies whether permissions are retained when the subscription is revoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeSubscriptionOutput) -> dict:
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


def deserialize_json(data: dict) -> RevokeSubscriptionOutput:
    out: RevokeSubscriptionOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RevokeSubscriptionOutput.id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("RevokeSubscriptionOutput.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("RevokeSubscriptionOutput.domain_id required")
    if "status" in data:
        import aws_sdk_datazone.types.subscription_status

        out["status"] = aws_sdk_datazone.types.subscription_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("RevokeSubscriptionOutput.status required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("RevokeSubscriptionOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("RevokeSubscriptionOutput.updated_at required")
    if "subscribedPrincipal" in data:
        import aws_sdk_datazone.types.subscribed_principal

        out["subscribed_principal"] = (
            aws_sdk_datazone.types.subscribed_principal.deserialize_json(
                data["subscribedPrincipal"]
            )
        )
    else:
        raise DeserializationError(
            "RevokeSubscriptionOutput.subscribed_principal required"
        )
    if "subscribedListing" in data:
        import aws_sdk_datazone.types.subscribed_listing

        out["subscribed_listing"] = (
            aws_sdk_datazone.types.subscribed_listing.deserialize_json(
                data["subscribedListing"]
            )
        )
    else:
        raise DeserializationError(
            "RevokeSubscriptionOutput.subscribed_listing required"
        )
    if "subscriptionRequestId" in data:
        out["subscription_request_id"] = data["subscriptionRequestId"]
    if "retainPermissions" in data:
        out["retain_permissions"] = data["retainPermissions"]
    return out

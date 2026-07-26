"""Generated from Smithy shape ``com.amazonaws.datazone#GetSubscriptionGrantOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.granted_entity
    import capo_datazone.types.subscribed_assets
    import capo_datazone.types.subscription_grant_id
    import capo_datazone.types.subscription_grant_overall_status
    import capo_datazone.types.subscription_id
    import capo_datazone.types.subscription_target_id
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class GetSubscriptionGrantOutput(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The ID of the subscription grant.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription grant.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription grant.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription grant exists.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription grant is created.</p>"""
    updated_at: "capo_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription grant was upated.</p>"""
    environment_id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The environment ID of the subscription grant.</p>"""
    subscription_target_id: (
        "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    )
    """<p>The subscription target ID associated with the subscription grant.</p>"""
    granted_entity: "capo_datazone.types.granted_entity.GrantedEntity"
    """<p>The entity to which the subscription is granted.</p>"""
    status: "capo_datazone.types.subscription_grant_overall_status.SubscriptionGrantOverallStatus"
    """<p>The status of the subscription grant.</p>"""
    assets: NotRequired["capo_datazone.types.subscribed_assets.SubscribedAssets"]
    """<p>The assets for which the subscription grant is created.</p>"""
    subscription_id: NotRequired["capo_datazone.types.subscription_id.SubscriptionId"]
    """<p>The identifier of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSubscriptionGrantOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import capo_datazone.types.updated_at

    out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    out["subscriptionTargetId"] = value["subscription_target_id"]
    import capo_datazone.types.granted_entity

    out["grantedEntity"] = capo_datazone.types.granted_entity.serialize_json(
        value["granted_entity"]
    )
    import capo_datazone.types.subscription_grant_overall_status

    out["status"] = (
        capo_datazone.types.subscription_grant_overall_status.serialize_json(
            value["status"]
        )
    )
    if "assets" in value:
        import capo_datazone.types.subscribed_assets

        out["assets"] = capo_datazone.types.subscribed_assets.serialize_json(
            value["assets"]
        )
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    return out


def deserialize_json(data: dict) -> GetSubscriptionGrantOutput:
    out: GetSubscriptionGrantOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.domain_id required")
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.created_at required")
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.updated_at required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "subscriptionTargetId" in data:
        out["subscription_target_id"] = data["subscriptionTargetId"]
    else:
        raise DeserializationError(
            "GetSubscriptionGrantOutput.subscription_target_id required"
        )
    if "grantedEntity" in data:
        import capo_datazone.types.granted_entity

        out["granted_entity"] = capo_datazone.types.granted_entity.deserialize_json(
            data["grantedEntity"]
        )
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.granted_entity required")
    if "status" in data:
        import capo_datazone.types.subscription_grant_overall_status

        out["status"] = (
            capo_datazone.types.subscription_grant_overall_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetSubscriptionGrantOutput.status required")
    if "assets" in data:
        import capo_datazone.types.subscribed_assets

        out["assets"] = capo_datazone.types.subscribed_assets.deserialize_json(
            data["assets"]
        )
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    return out

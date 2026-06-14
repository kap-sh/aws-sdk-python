"""Generated from Smithy shape ``com.amazonaws.datazone#CreateSubscriptionGrantOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.granted_entity
    import aws_sdk_datazone.types.subscribed_assets
    import aws_sdk_datazone.types.subscription_grant_id
    import aws_sdk_datazone.types.subscription_grant_overall_status
    import aws_sdk_datazone.types.subscription_id
    import aws_sdk_datazone.types.subscription_target_id
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class CreateSubscriptionGrantOutput(TypedDict):
    id: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The ID of the subscription grant.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription grant.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription grant.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription grant is created.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>A timestamp of when the subscription grant is created.</p>"""
    updated_at: "aws_sdk_datazone.types.updated_at.UpdatedAt"
    """<p>A timestamp of when the subscription grant was updated.</p>"""
    environment_id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The environment ID for which subscription grant is created.</p>"""
    subscription_target_id: (
        "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
    )
    """<p>The ID of the subscription target for which the subscription grant is created.</p>"""
    granted_entity: "aws_sdk_datazone.types.granted_entity.GrantedEntity"
    """<p>The entity to which the subscription is granted.</p>"""
    status: "aws_sdk_datazone.types.subscription_grant_overall_status.SubscriptionGrantOverallStatus"
    """<p>The status of the subscription grant.</p>"""
    assets: NotRequired["aws_sdk_datazone.types.subscribed_assets.SubscribedAssets"]
    """<p>The assets for which the subscription grant is created.</p>"""
    subscription_id: NotRequired[
        "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    ]
    """<p>The identifier of the subscription grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionGrantOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["domainId"] = value["domain_id"]
    import aws_sdk_datazone.types.created_at

    out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    import aws_sdk_datazone.types.updated_at

    out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
        value["updated_at"]
    )
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    out["subscriptionTargetId"] = value["subscription_target_id"]
    import aws_sdk_datazone.types.granted_entity

    out["grantedEntity"] = aws_sdk_datazone.types.granted_entity.serialize_json(
        value["granted_entity"]
    )
    import aws_sdk_datazone.types.subscription_grant_overall_status

    out["status"] = (
        aws_sdk_datazone.types.subscription_grant_overall_status.serialize_json(
            value["status"]
        )
    )
    if "assets" in value:
        import aws_sdk_datazone.types.subscribed_assets

        out["assets"] = aws_sdk_datazone.types.subscribed_assets.serialize_json(
            value["assets"]
        )
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    return out


def deserialize_json(data: dict) -> CreateSubscriptionGrantOutput:
    out: CreateSubscriptionGrantOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateSubscriptionGrantOutput.id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateSubscriptionGrantOutput.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateSubscriptionGrantOutput.domain_id required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateSubscriptionGrantOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreateSubscriptionGrantOutput.updated_at required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "subscriptionTargetId" in data:
        out["subscription_target_id"] = data["subscriptionTargetId"]
    else:
        raise DeserializationError(
            "CreateSubscriptionGrantOutput.subscription_target_id required"
        )
    if "grantedEntity" in data:
        import aws_sdk_datazone.types.granted_entity

        out["granted_entity"] = aws_sdk_datazone.types.granted_entity.deserialize_json(
            data["grantedEntity"]
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionGrantOutput.granted_entity required"
        )
    if "status" in data:
        import aws_sdk_datazone.types.subscription_grant_overall_status

        out["status"] = (
            aws_sdk_datazone.types.subscription_grant_overall_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateSubscriptionGrantOutput.status required")
    if "assets" in data:
        import aws_sdk_datazone.types.subscribed_assets

        out["assets"] = aws_sdk_datazone.types.subscribed_assets.deserialize_json(
            data["assets"]
        )
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    return out

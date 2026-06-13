"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteSubscriptionGrantOutput``."""

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


class DeleteSubscriptionGrantOutput(TypedDict):
    id: "aws_sdk_datazone.types.subscription_grant_id.SubscriptionGrantId"
    """<p>The ID of the subscription grant that is deleted.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription grant that is deleted.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription grant that is deleted.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription grant is deleted.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription grant that is deleted was created.</p>"""
    updated_at: "aws_sdk_datazone.types.updated_at.UpdatedAt"
    """<p>The timestamp of when the subscription grant that is deleted was updated.</p>"""
    environment_id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment in which the subscription grant is deleted.</p>"""
    subscription_target_id: (
        "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
    )
    """<p>The ID of the subscription target associated with the subscription grant that is deleted.</p>"""
    granted_entity: "aws_sdk_datazone.types.granted_entity.GrantedEntity"
    """<p>The entity to which the subscription is deleted.</p>"""
    status: "aws_sdk_datazone.types.subscription_grant_overall_status.SubscriptionGrantOverallStatus"
    """<p>The status of the subscription grant that is deleted.</p>"""
    assets: NotRequired["aws_sdk_datazone.types.subscribed_assets.SubscribedAssets"]
    """<p>The assets for which the subsctiption grant that is deleted gave access.</p>"""
    subscription_id: NotRequired[
        "aws_sdk_datazone.types.subscription_id.SubscriptionId"
    ]
    """<p>The identifier of the subsctiption whose subscription grant is to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSubscriptionGrantOutput) -> dict:
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


def deserialize_json(data: dict) -> DeleteSubscriptionGrantOutput:
    out: DeleteSubscriptionGrantOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteSubscriptionGrantOutput.id required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("DeleteSubscriptionGrantOutput.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("DeleteSubscriptionGrantOutput.domain_id required")
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("DeleteSubscriptionGrantOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("DeleteSubscriptionGrantOutput.updated_at required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "subscriptionTargetId" in data:
        out["subscription_target_id"] = data["subscriptionTargetId"]
    else:
        raise DeserializationError(
            "DeleteSubscriptionGrantOutput.subscription_target_id required"
        )
    if "grantedEntity" in data:
        import aws_sdk_datazone.types.granted_entity

        out["granted_entity"] = aws_sdk_datazone.types.granted_entity.deserialize_json(
            data["grantedEntity"]
        )
    else:
        raise DeserializationError(
            "DeleteSubscriptionGrantOutput.granted_entity required"
        )
    if "status" in data:
        import aws_sdk_datazone.types.subscription_grant_overall_status

        out["status"] = (
            aws_sdk_datazone.types.subscription_grant_overall_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteSubscriptionGrantOutput.status required")
    if "assets" in data:
        import aws_sdk_datazone.types.subscribed_assets

        out["assets"] = aws_sdk_datazone.types.subscribed_assets.deserialize_json(
            data["assets"]
        )
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    return out

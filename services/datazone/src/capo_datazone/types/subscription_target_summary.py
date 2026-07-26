"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionTargetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.applicable_asset_types
    import capo_datazone.types.authorized_principal_identifiers
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_id
    import capo_datazone.types.iam_role_arn
    import capo_datazone.types.project_id
    import capo_datazone.types.subscription_grant_creation_mode
    import capo_datazone.types.subscription_target_forms
    import capo_datazone.types.subscription_target_id
    import capo_datazone.types.subscription_target_name
    import capo_datazone.types.updated_at
    import capo_datazone.types.updated_by


class SubscriptionTargetSummary(TypedDict, closed=True):
    id: "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The identifier of the subscription target.</p>"""
    authorized_principals: "capo_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
    """<p>The authorized principals included in the subscription target.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the subscription target exists.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project specified in the subscription target.</p>"""
    environment_id: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment of the subscription target.</p>"""
    name: "capo_datazone.types.subscription_target_name.SubscriptionTargetName"
    """<p>The name of the subscription target.</p>"""
    type: "str"
    """<p>The type of the subscription target.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription target.</p>"""
    updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription target.</p>"""
    created_at: "capo_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription target was created.</p>"""
    updated_at: NotRequired["capo_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the subscription target was updated.</p>"""
    manage_access_role: NotRequired["capo_datazone.types.iam_role_arn.IamRoleArn"]
    """<p>The manage access role specified in the subscription target.</p>"""
    applicable_asset_types: (
        "capo_datazone.types.applicable_asset_types.ApplicableAssetTypes"
    )
    """<p>The asset types included in the subscription target.</p>"""
    subscription_target_config: (
        "capo_datazone.types.subscription_target_forms.SubscriptionTargetForms"
    )
    """<p>The configuration of the subscription target.</p>"""
    provider: "str"
    """<p>The provider of the subscription target.</p>"""
    subscription_grant_creation_mode: NotRequired[
        "capo_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
    ]
    """<p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionTargetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_datazone.types.authorized_principal_identifiers

    out["authorizedPrincipals"] = (
        capo_datazone.types.authorized_principal_identifiers.serialize_json(
            value["authorized_principals"]
        )
    )
    out["domainId"] = value["domain_id"]
    out["projectId"] = value["project_id"]
    out["environmentId"] = value["environment_id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["createdBy"] = value["created_by"]
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    import capo_datazone.types.created_at

    out["createdAt"] = capo_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_datazone.types.updated_at

        out["updatedAt"] = capo_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "manage_access_role" in value:
        out["manageAccessRole"] = value["manage_access_role"]
    import capo_datazone.types.applicable_asset_types

    out["applicableAssetTypes"] = (
        capo_datazone.types.applicable_asset_types.serialize_json(
            value["applicable_asset_types"]
        )
    )
    import capo_datazone.types.subscription_target_forms

    out["subscriptionTargetConfig"] = (
        capo_datazone.types.subscription_target_forms.serialize_json(
            value["subscription_target_config"]
        )
    )
    out["provider"] = value["provider"]
    if "subscription_grant_creation_mode" in value:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscriptionGrantCreationMode"] = (
            capo_datazone.types.subscription_grant_creation_mode.serialize_json(
                value["subscription_grant_creation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscriptionTargetSummary:
    out: SubscriptionTargetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.id required")
    if "authorizedPrincipals" in data:
        import capo_datazone.types.authorized_principal_identifiers

        out["authorized_principals"] = (
            capo_datazone.types.authorized_principal_identifiers.deserialize_json(
                data["authorizedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionTargetSummary.authorized_principals required"
        )
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.domain_id required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.project_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.environment_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.type required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "createdAt" in data:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("SubscriptionTargetSummary.created_at required")
    if "updatedAt" in data:
        import capo_datazone.types.updated_at

        out["updated_at"] = capo_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "manageAccessRole" in data:
        out["manage_access_role"] = data["manageAccessRole"]
    if "applicableAssetTypes" in data:
        import capo_datazone.types.applicable_asset_types

        out["applicable_asset_types"] = (
            capo_datazone.types.applicable_asset_types.deserialize_json(
                data["applicableAssetTypes"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionTargetSummary.applicable_asset_types required"
        )
    if "subscriptionTargetConfig" in data:
        import capo_datazone.types.subscription_target_forms

        out["subscription_target_config"] = (
            capo_datazone.types.subscription_target_forms.deserialize_json(
                data["subscriptionTargetConfig"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionTargetSummary.subscription_target_config required"
        )
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("SubscriptionTargetSummary.provider required")
    if "subscriptionGrantCreationMode" in data:
        import capo_datazone.types.subscription_grant_creation_mode

        out["subscription_grant_creation_mode"] = (
            capo_datazone.types.subscription_grant_creation_mode.deserialize_json(
                data["subscriptionGrantCreationMode"]
            )
        )
    return out

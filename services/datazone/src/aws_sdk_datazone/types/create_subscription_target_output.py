"""Generated from Smithy shape ``com.amazonaws.datazone#CreateSubscriptionTargetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.applicable_asset_types
    import aws_sdk_datazone.types.authorized_principal_identifiers
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.iam_role_arn
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.subscription_grant_creation_mode
    import aws_sdk_datazone.types.subscription_target_forms
    import aws_sdk_datazone.types.subscription_target_id
    import aws_sdk_datazone.types.subscription_target_name
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class CreateSubscriptionTargetOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.subscription_target_id.SubscriptionTargetId"
    """<p>The ID of the subscription target.</p>"""
    authorized_principals: "aws_sdk_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
    """<p>The authorised principals of the subscription target.</p>"""
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription target was created.</p>"""
    project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>???</p>"""
    environment_id: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment in which the subscription target was created.</p>"""
    name: "aws_sdk_datazone.types.subscription_target_name.SubscriptionTargetName"
    """<p>The name of the subscription target.</p>"""
    type: "str"
    """<p>The type of the subscription target.</p>"""
    created_by: "aws_sdk_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the subscription target.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The Amazon DataZone user who updated the subscription target.</p>"""
    created_at: "aws_sdk_datazone.types.created_at.CreatedAt"
    """<p>The timestamp of when the subscription target was created.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp of when the subscription target was updated.</p>"""
    manage_access_role: NotRequired["aws_sdk_datazone.types.iam_role_arn.IamRoleArn"]
    """<p>The manage access role with which the subscription target was created.</p>"""
    applicable_asset_types: (
        "aws_sdk_datazone.types.applicable_asset_types.ApplicableAssetTypes"
    )
    """<p>The asset types that can be included in the subscription target.</p>"""
    subscription_target_config: (
        "aws_sdk_datazone.types.subscription_target_forms.SubscriptionTargetForms"
    )
    """<p>The configuration of the subscription target.</p>"""
    provider: "str"
    """<p>The provider of the subscription target.</p>"""
    subscription_grant_creation_mode: NotRequired[
        "aws_sdk_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
    ]
    """<p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionTargetOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_datazone.types.authorized_principal_identifiers

    out["authorizedPrincipals"] = (
        aws_sdk_datazone.types.authorized_principal_identifiers.serialize_json(
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
    import aws_sdk_datazone.types.created_at

    out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "manage_access_role" in value:
        out["manageAccessRole"] = value["manage_access_role"]
    import aws_sdk_datazone.types.applicable_asset_types

    out["applicableAssetTypes"] = (
        aws_sdk_datazone.types.applicable_asset_types.serialize_json(
            value["applicable_asset_types"]
        )
    )
    import aws_sdk_datazone.types.subscription_target_forms

    out["subscriptionTargetConfig"] = (
        aws_sdk_datazone.types.subscription_target_forms.serialize_json(
            value["subscription_target_config"]
        )
    )
    out["provider"] = value["provider"]
    if "subscription_grant_creation_mode" in value:
        import aws_sdk_datazone.types.subscription_grant_creation_mode

        out["subscriptionGrantCreationMode"] = (
            aws_sdk_datazone.types.subscription_grant_creation_mode.serialize_json(
                value["subscription_grant_creation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriptionTargetOutput:
    out: CreateSubscriptionTargetOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.id required")
    if "authorizedPrincipals" in data:
        import aws_sdk_datazone.types.authorized_principal_identifiers

        out["authorized_principals"] = (
            aws_sdk_datazone.types.authorized_principal_identifiers.deserialize_json(
                data["authorizedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetOutput.authorized_principals required"
        )
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.domain_id required")
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.project_id required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetOutput.environment_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.type required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.created_by required")
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "manageAccessRole" in data:
        out["manage_access_role"] = data["manageAccessRole"]
    if "applicableAssetTypes" in data:
        import aws_sdk_datazone.types.applicable_asset_types

        out["applicable_asset_types"] = (
            aws_sdk_datazone.types.applicable_asset_types.deserialize_json(
                data["applicableAssetTypes"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetOutput.applicable_asset_types required"
        )
    if "subscriptionTargetConfig" in data:
        import aws_sdk_datazone.types.subscription_target_forms

        out["subscription_target_config"] = (
            aws_sdk_datazone.types.subscription_target_forms.deserialize_json(
                data["subscriptionTargetConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetOutput.subscription_target_config required"
        )
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("CreateSubscriptionTargetOutput.provider required")
    if "subscriptionGrantCreationMode" in data:
        import aws_sdk_datazone.types.subscription_grant_creation_mode

        out["subscription_grant_creation_mode"] = (
            aws_sdk_datazone.types.subscription_grant_creation_mode.deserialize_json(
                data["subscriptionGrantCreationMode"]
            )
        )
    return out

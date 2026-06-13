"""Generated from Smithy shape ``com.amazonaws.datazone#CreateSubscriptionTargetInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.applicable_asset_types
    import aws_sdk_datazone.types.authorized_principal_identifiers
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.iam_role_arn
    import aws_sdk_datazone.types.subscription_grant_creation_mode
    import aws_sdk_datazone.types.subscription_target_forms
    import aws_sdk_datazone.types.subscription_target_name


class CreateSubscriptionTargetInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which subscription target is created.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment in which subscription target is created.</p>"""
    name: "aws_sdk_datazone.types.subscription_target_name.SubscriptionTargetName"
    """<p>The name of the subscription target.</p>"""
    type: "str"
    """<p>The type of the subscription target.</p>"""
    subscription_target_config: (
        "aws_sdk_datazone.types.subscription_target_forms.SubscriptionTargetForms"
    )
    """<p>The configuration of the subscription target.</p>"""
    authorized_principals: "aws_sdk_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
    """<p>The authorized principals of the subscription target.</p>"""
    manage_access_role: "aws_sdk_datazone.types.iam_role_arn.IamRoleArn"
    """<p>The manage access role that is used to create the subscription target.</p>"""
    applicable_asset_types: (
        "aws_sdk_datazone.types.applicable_asset_types.ApplicableAssetTypes"
    )
    """<p>The asset types that can be included in the subscription target.</p>"""
    provider: NotRequired["str"]
    """<p>The provider of the subscription target.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    subscription_grant_creation_mode: NotRequired[
        "aws_sdk_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
    ]
    """<p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionTargetInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    import aws_sdk_datazone.types.subscription_target_forms

    out["subscriptionTargetConfig"] = (
        aws_sdk_datazone.types.subscription_target_forms.serialize_json(
            value["subscription_target_config"]
        )
    )
    import aws_sdk_datazone.types.authorized_principal_identifiers

    out["authorizedPrincipals"] = (
        aws_sdk_datazone.types.authorized_principal_identifiers.serialize_json(
            value["authorized_principals"]
        )
    )
    out["manageAccessRole"] = value["manage_access_role"]
    import aws_sdk_datazone.types.applicable_asset_types

    out["applicableAssetTypes"] = (
        aws_sdk_datazone.types.applicable_asset_types.serialize_json(
            value["applicable_asset_types"]
        )
    )
    if "provider" in value:
        out["provider"] = value["provider"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "subscription_grant_creation_mode" in value:
        import aws_sdk_datazone.types.subscription_grant_creation_mode

        out["subscriptionGrantCreationMode"] = (
            aws_sdk_datazone.types.subscription_grant_creation_mode.serialize_json(
                value["subscription_grant_creation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriptionTargetInput:
    out: CreateSubscriptionTargetInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSubscriptionTargetInput.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateSubscriptionTargetInput.type required")
    if "subscriptionTargetConfig" in data:
        import aws_sdk_datazone.types.subscription_target_forms

        out["subscription_target_config"] = (
            aws_sdk_datazone.types.subscription_target_forms.deserialize_json(
                data["subscriptionTargetConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetInput.subscription_target_config required"
        )
    if "authorizedPrincipals" in data:
        import aws_sdk_datazone.types.authorized_principal_identifiers

        out["authorized_principals"] = (
            aws_sdk_datazone.types.authorized_principal_identifiers.deserialize_json(
                data["authorizedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetInput.authorized_principals required"
        )
    if "manageAccessRole" in data:
        out["manage_access_role"] = data["manageAccessRole"]
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetInput.manage_access_role required"
        )
    if "applicableAssetTypes" in data:
        import aws_sdk_datazone.types.applicable_asset_types

        out["applicable_asset_types"] = (
            aws_sdk_datazone.types.applicable_asset_types.deserialize_json(
                data["applicableAssetTypes"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionTargetInput.applicable_asset_types required"
        )
    if "provider" in data:
        out["provider"] = data["provider"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "subscriptionGrantCreationMode" in data:
        import aws_sdk_datazone.types.subscription_grant_creation_mode

        out["subscription_grant_creation_mode"] = (
            aws_sdk_datazone.types.subscription_grant_creation_mode.deserialize_json(
                data["subscriptionGrantCreationMode"]
            )
        )
    return out

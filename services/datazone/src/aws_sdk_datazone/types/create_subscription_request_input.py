"""Generated from Smithy shape ``com.amazonaws.datazone#CreateSubscriptionRequestInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.accepted_asset_scopes
    import aws_sdk_datazone.types.asset_permissions
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.metadata_form_inputs
    import aws_sdk_datazone.types.request_reason
    import aws_sdk_datazone.types.subscribed_listing_inputs
    import aws_sdk_datazone.types.subscribed_principal_inputs


class CreateSubscriptionRequestInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the subscription request is created.</p>"""
    subscribed_principals: (
        "aws_sdk_datazone.types.subscribed_principal_inputs.SubscribedPrincipalInputs"
    )
    """<p>The Amazon DataZone principals for whom the subscription request is created.</p>"""
    subscribed_listings: (
        "aws_sdk_datazone.types.subscribed_listing_inputs.SubscribedListingInputs"
    )
    """<p>The published asset for which the subscription grant is to be created.</p>"""
    request_reason: "aws_sdk_datazone.types.request_reason.RequestReason"
    """<p>The reason for the subscription request.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    metadata_forms: NotRequired[
        "aws_sdk_datazone.types.metadata_form_inputs.MetadataFormInputs"
    ]
    """<p>The metadata form included in the subscription request.</p>"""
    asset_permissions: NotRequired[
        "aws_sdk_datazone.types.asset_permissions.AssetPermissions"
    ]
    """<p>The asset permissions of the subscription request.</p>"""
    asset_scopes: NotRequired[
        "aws_sdk_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
    ]
    """<p>The asset scopes of the subscription request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionRequestInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.subscribed_principal_inputs

    out["subscribedPrincipals"] = (
        aws_sdk_datazone.types.subscribed_principal_inputs.serialize_json(
            value["subscribed_principals"]
        )
    )
    import aws_sdk_datazone.types.subscribed_listing_inputs

    out["subscribedListings"] = (
        aws_sdk_datazone.types.subscribed_listing_inputs.serialize_json(
            value["subscribed_listings"]
        )
    )
    out["requestReason"] = value["request_reason"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "metadata_forms" in value:
        import aws_sdk_datazone.types.metadata_form_inputs

        out["metadataForms"] = (
            aws_sdk_datazone.types.metadata_form_inputs.serialize_json(
                value["metadata_forms"]
            )
        )
    if "asset_permissions" in value:
        import aws_sdk_datazone.types.asset_permissions

        out["assetPermissions"] = (
            aws_sdk_datazone.types.asset_permissions.serialize_json(
                value["asset_permissions"]
            )
        )
    if "asset_scopes" in value:
        import aws_sdk_datazone.types.accepted_asset_scopes

        out["assetScopes"] = (
            aws_sdk_datazone.types.accepted_asset_scopes.serialize_json(
                value["asset_scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSubscriptionRequestInput:
    out: CreateSubscriptionRequestInput = {}  # type: ignore[typeddict-item]
    if "subscribedPrincipals" in data:
        import aws_sdk_datazone.types.subscribed_principal_inputs

        out["subscribed_principals"] = (
            aws_sdk_datazone.types.subscribed_principal_inputs.deserialize_json(
                data["subscribedPrincipals"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionRequestInput.subscribed_principals required"
        )
    if "subscribedListings" in data:
        import aws_sdk_datazone.types.subscribed_listing_inputs

        out["subscribed_listings"] = (
            aws_sdk_datazone.types.subscribed_listing_inputs.deserialize_json(
                data["subscribedListings"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriptionRequestInput.subscribed_listings required"
        )
    if "requestReason" in data:
        out["request_reason"] = data["requestReason"]
    else:
        raise DeserializationError(
            "CreateSubscriptionRequestInput.request_reason required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "metadataForms" in data:
        import aws_sdk_datazone.types.metadata_form_inputs

        out["metadata_forms"] = (
            aws_sdk_datazone.types.metadata_form_inputs.deserialize_json(
                data["metadataForms"]
            )
        )
    if "assetPermissions" in data:
        import aws_sdk_datazone.types.asset_permissions

        out["asset_permissions"] = (
            aws_sdk_datazone.types.asset_permissions.deserialize_json(
                data["assetPermissions"]
            )
        )
    if "assetScopes" in data:
        import aws_sdk_datazone.types.accepted_asset_scopes

        out["asset_scopes"] = (
            aws_sdk_datazone.types.accepted_asset_scopes.deserialize_json(
                data["assetScopes"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutAssetModelInterfaceRelationshipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.client_token
    import aws_sdk_iotsitewise.types.custom_id
    import aws_sdk_iotsitewise.types.property_mapping_configuration


class PutAssetModelInterfaceRelationshipRequest(TypedDict, closed=True):
    asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""
    interface_asset_model_id: "aws_sdk_iotsitewise.types.custom_id.CustomID"
    """<p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>"""
    property_mapping_configuration: "aws_sdk_iotsitewise.types.property_mapping_configuration.PropertyMappingConfiguration"
    """<p>The configuration for mapping properties from the interface asset model to the asset model where the interface is applied. This configuration controls how properties are matched and created during the interface application process.</p>"""
    client_token: NotRequired["aws_sdk_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAssetModelInterfaceRelationshipRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.property_mapping_configuration

    out["propertyMappingConfiguration"] = (
        aws_sdk_iotsitewise.types.property_mapping_configuration.serialize_json(
            value["property_mapping_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutAssetModelInterfaceRelationshipRequest:
    out: PutAssetModelInterfaceRelationshipRequest = {}  # type: ignore[typeddict-item]
    if "propertyMappingConfiguration" in data:
        import aws_sdk_iotsitewise.types.property_mapping_configuration

        out["property_mapping_configuration"] = (
            aws_sdk_iotsitewise.types.property_mapping_configuration.deserialize_json(
                data["propertyMappingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutAssetModelInterfaceRelationshipRequest.property_mapping_configuration required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

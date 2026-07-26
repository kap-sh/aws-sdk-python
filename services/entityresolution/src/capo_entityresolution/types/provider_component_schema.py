"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderComponentSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.provider_schema_attributes
    import capo_entityresolution.types.schemas


class ProviderComponentSchema(TypedDict, closed=True):
    schemas: NotRequired["capo_entityresolution.types.schemas.Schemas"]
    """<p>Input schema for the provider service.</p>"""
    provider_schema_attributes: NotRequired[
        "capo_entityresolution.types.provider_schema_attributes.ProviderSchemaAttributes"
    ]
    """<p>The provider schema attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderComponentSchema) -> dict:
    out: dict = {}
    if "schemas" in value:
        import capo_entityresolution.types.schemas

        out["schemas"] = capo_entityresolution.types.schemas.serialize_json(
            value["schemas"]
        )
    if "provider_schema_attributes" in value:
        import capo_entityresolution.types.provider_schema_attributes

        out["providerSchemaAttributes"] = (
            capo_entityresolution.types.provider_schema_attributes.serialize_json(
                value["provider_schema_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProviderComponentSchema:
    out: ProviderComponentSchema = {}  # type: ignore[typeddict-item]
    if "schemas" in data:
        import capo_entityresolution.types.schemas

        out["schemas"] = capo_entityresolution.types.schemas.deserialize_json(
            data["schemas"]
        )
    if "providerSchemaAttributes" in data:
        import capo_entityresolution.types.provider_schema_attributes

        out["provider_schema_attributes"] = (
            capo_entityresolution.types.provider_schema_attributes.deserialize_json(
                data["providerSchemaAttributes"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeyUsageProperty``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pca_connector_ad.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.key_usage_property_flags
    import capo_pca_connector_ad.types.key_usage_property_type


class _KeyUsageProperty_PropertyType(TypedDict, closed=True):
    PropertyType: (
        "capo_pca_connector_ad.types.key_usage_property_type.KeyUsagePropertyType"
    )


class _KeyUsageProperty_PropertyFlags(TypedDict, closed=True):
    PropertyFlags: (
        "capo_pca_connector_ad.types.key_usage_property_flags.KeyUsagePropertyFlags"
    )


KeyUsageProperty: TypeAlias = (
    _KeyUsageProperty_PropertyType | _KeyUsageProperty_PropertyFlags
)


# --- restJson1 ser/de ---
def serialize_json(value: KeyUsageProperty) -> dict:
    if "PropertyType" in value:
        import capo_pca_connector_ad.types.key_usage_property_type

        return {
            "PropertyType": capo_pca_connector_ad.types.key_usage_property_type.serialize_json(
                value["PropertyType"]
            )
        }
    elif "PropertyFlags" in value:
        import capo_pca_connector_ad.types.key_usage_property_flags

        return {
            "PropertyFlags": capo_pca_connector_ad.types.key_usage_property_flags.serialize_json(
                value["PropertyFlags"]
            )
        }
    else:
        raise SerializationError("KeyUsageProperty: no variant present")


def deserialize_json(data: dict) -> KeyUsageProperty:
    if "PropertyType" in data:
        import capo_pca_connector_ad.types.key_usage_property_type

        return {
            "PropertyType": capo_pca_connector_ad.types.key_usage_property_type.deserialize_json(
                data["PropertyType"]
            )
        }
    elif "PropertyFlags" in data:
        import capo_pca_connector_ad.types.key_usage_property_flags

        return {
            "PropertyFlags": capo_pca_connector_ad.types.key_usage_property_flags.deserialize_json(
                data["PropertyFlags"]
            )
        }
    else:
        raise DeserializationError("KeyUsageProperty: no recognized variant key")

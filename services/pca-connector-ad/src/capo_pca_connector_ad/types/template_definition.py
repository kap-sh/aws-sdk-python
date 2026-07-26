"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pca_connector_ad.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.template_v2
    import capo_pca_connector_ad.types.template_v3
    import capo_pca_connector_ad.types.template_v4


class _TemplateDefinition_TemplateV2(TypedDict, closed=True):
    TemplateV2: "capo_pca_connector_ad.types.template_v2.TemplateV2"


class _TemplateDefinition_TemplateV3(TypedDict, closed=True):
    TemplateV3: "capo_pca_connector_ad.types.template_v3.TemplateV3"


class _TemplateDefinition_TemplateV4(TypedDict, closed=True):
    TemplateV4: "capo_pca_connector_ad.types.template_v4.TemplateV4"


TemplateDefinition: TypeAlias = (
    _TemplateDefinition_TemplateV2
    | _TemplateDefinition_TemplateV3
    | _TemplateDefinition_TemplateV4
)


# --- restJson1 ser/de ---
def serialize_json(value: TemplateDefinition) -> dict:
    if "TemplateV2" in value:
        import capo_pca_connector_ad.types.template_v2

        return {
            "TemplateV2": capo_pca_connector_ad.types.template_v2.serialize_json(
                value["TemplateV2"]
            )
        }
    elif "TemplateV3" in value:
        import capo_pca_connector_ad.types.template_v3

        return {
            "TemplateV3": capo_pca_connector_ad.types.template_v3.serialize_json(
                value["TemplateV3"]
            )
        }
    elif "TemplateV4" in value:
        import capo_pca_connector_ad.types.template_v4

        return {
            "TemplateV4": capo_pca_connector_ad.types.template_v4.serialize_json(
                value["TemplateV4"]
            )
        }
    else:
        raise SerializationError("TemplateDefinition: no variant present")


def deserialize_json(data: dict) -> TemplateDefinition:
    if "TemplateV2" in data:
        import capo_pca_connector_ad.types.template_v2

        return {
            "TemplateV2": capo_pca_connector_ad.types.template_v2.deserialize_json(
                data["TemplateV2"]
            )
        }
    elif "TemplateV3" in data:
        import capo_pca_connector_ad.types.template_v3

        return {
            "TemplateV3": capo_pca_connector_ad.types.template_v3.deserialize_json(
                data["TemplateV3"]
            )
        }
    elif "TemplateV4" in data:
        import capo_pca_connector_ad.types.template_v4

        return {
            "TemplateV4": capo_pca_connector_ad.types.template_v4.deserialize_json(
                data["TemplateV4"]
            )
        }
    else:
        raise DeserializationError("TemplateDefinition: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.appflow#MetadataCatalogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.glue_data_catalog_config


class MetadataCatalogConfig(TypedDict, closed=True):
    glue_data_catalog: NotRequired[
        "capo_appflow.types.glue_data_catalog_config.GlueDataCatalogConfig"
    ]
    """<p>Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the Glue Data Catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataCatalogConfig) -> dict:
    out: dict = {}
    if "glue_data_catalog" in value:
        import capo_appflow.types.glue_data_catalog_config

        out["glueDataCatalog"] = (
            capo_appflow.types.glue_data_catalog_config.serialize_json(
                value["glue_data_catalog"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataCatalogConfig:
    out: MetadataCatalogConfig = {}  # type: ignore[typeddict-item]
    if "glueDataCatalog" in data:
        import capo_appflow.types.glue_data_catalog_config

        out["glue_data_catalog"] = (
            capo_appflow.types.glue_data_catalog_config.deserialize_json(
                data["glueDataCatalog"]
            )
        )
    return out

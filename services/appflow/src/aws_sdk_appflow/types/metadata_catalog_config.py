"""Generated from Smithy shape ``com.amazonaws.appflow#MetadataCatalogConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.glue_data_catalog_config


class MetadataCatalogConfig(TypedDict):
    glue_data_catalog: NotRequired[
        "aws_sdk_appflow.types.glue_data_catalog_config.GlueDataCatalogConfig"
    ]
    """<p>Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the Glue Data Catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataCatalogConfig) -> dict:
    out: dict = {}
    if "glue_data_catalog" in value:
        import aws_sdk_appflow.types.glue_data_catalog_config

        out["glueDataCatalog"] = (
            aws_sdk_appflow.types.glue_data_catalog_config.serialize_json(
                value["glue_data_catalog"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataCatalogConfig:
    out: MetadataCatalogConfig = {}  # type: ignore[typeddict-item]
    if "glueDataCatalog" in data:
        import aws_sdk_appflow.types.glue_data_catalog_config

        out["glue_data_catalog"] = (
            aws_sdk_appflow.types.glue_data_catalog_config.deserialize_json(
                data["glueDataCatalog"]
            )
        )
    return out

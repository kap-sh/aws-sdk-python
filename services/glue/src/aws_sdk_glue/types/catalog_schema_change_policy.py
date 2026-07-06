"""Generated from Smithy shape ``com.amazonaws.glue#CatalogSchemaChangePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.boxed_boolean
    import aws_sdk_glue.types.update_catalog_behavior


class CatalogSchemaChangePolicy(TypedDict, closed=True):
    enable_update_catalog: NotRequired["aws_sdk_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether to use the specified update behavior when the crawler finds a changed schema.</p>"""
    update_behavior: NotRequired[
        "aws_sdk_glue.types.update_catalog_behavior.UpdateCatalogBehavior"
    ]
    """<p>The update behavior when the crawler finds a changed schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogSchemaChangePolicy) -> dict:
    out: dict = {}
    if "enable_update_catalog" in value:
        out["EnableUpdateCatalog"] = value["enable_update_catalog"]
    if "update_behavior" in value:
        import aws_sdk_glue.types.update_catalog_behavior

        out["UpdateBehavior"] = (
            aws_sdk_glue.types.update_catalog_behavior.serialize_aws_json_1_1(
                value["update_behavior"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogSchemaChangePolicy:
    out: CatalogSchemaChangePolicy = {}  # type: ignore[typeddict-item]
    if "EnableUpdateCatalog" in data:
        out["enable_update_catalog"] = data["EnableUpdateCatalog"]
    if "UpdateBehavior" in data:
        import aws_sdk_glue.types.update_catalog_behavior

        out["update_behavior"] = (
            aws_sdk_glue.types.update_catalog_behavior.deserialize_aws_json_1_1(
                data["UpdateBehavior"]
            )
        )
    return out

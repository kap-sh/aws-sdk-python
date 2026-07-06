"""Generated from Smithy shape ``com.amazonaws.glue#CreateCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_input
    import aws_sdk_glue.types.catalog_name_string
    import aws_sdk_glue.types.tags_map


class CreateCatalogRequest(TypedDict, closed=True):
    name: "aws_sdk_glue.types.catalog_name_string.CatalogNameString"
    """<p>The name of the catalog to create.</p>"""
    catalog_input: "aws_sdk_glue.types.catalog_input.CatalogInput"
    """<p>A <code>CatalogInput</code> object that defines the metadata for the catalog.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>A map array of key-value pairs, not more than 50 pairs. Each key is a UTF-8 string, not less than 1 or more than 128 bytes long. Each value is a UTF-8 string, not more than 256 bytes long. The tags you assign to the catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCatalogRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.catalog_input

    out["CatalogInput"] = aws_sdk_glue.types.catalog_input.serialize_aws_json_1_1(
        value["catalog_input"]
    )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCatalogRequest:
    out: CreateCatalogRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateCatalogRequest.name required")
    if "CatalogInput" in data:
        import aws_sdk_glue.types.catalog_input

        out["catalog_input"] = (
            aws_sdk_glue.types.catalog_input.deserialize_aws_json_1_1(
                data["CatalogInput"]
            )
        )
    else:
        raise DeserializationError("CreateCatalogRequest.catalog_input required")
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out

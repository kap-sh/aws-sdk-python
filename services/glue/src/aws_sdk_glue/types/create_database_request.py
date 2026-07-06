"""Generated from Smithy shape ``com.amazonaws.glue#CreateDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.database_input
    import aws_sdk_glue.types.tags_map


class CreateDatabaseRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which to create the database. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_input: "aws_sdk_glue.types.database_input.DatabaseInput"
    """<p>The metadata for the database.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>The tags you assign to the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatabaseRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import aws_sdk_glue.types.database_input

    out["DatabaseInput"] = aws_sdk_glue.types.database_input.serialize_aws_json_1_1(
        value["database_input"]
    )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatabaseRequest:
    out: CreateDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseInput" in data:
        import aws_sdk_glue.types.database_input

        out["database_input"] = (
            aws_sdk_glue.types.database_input.deserialize_aws_json_1_1(
                data["DatabaseInput"]
            )
        )
    else:
        raise DeserializationError("CreateDatabaseRequest.database_input required")
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out

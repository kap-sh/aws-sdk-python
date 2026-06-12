"""Generated from Smithy shape ``com.amazonaws.glue#CreateConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.connection_input
    import aws_sdk_glue.types.tags_map


class CreateConnectionRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which to create the connection. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    connection_input: "aws_sdk_glue.types.connection_input.ConnectionInput"
    """<p>A <code>ConnectionInput</code> object defining the connection to create.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>The tags you assign to the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import aws_sdk_glue.types.connection_input

    out["ConnectionInput"] = aws_sdk_glue.types.connection_input.serialize_aws_json_1_1(
        value["connection_input"]
    )
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "ConnectionInput" in data:
        import aws_sdk_glue.types.connection_input

        out["connection_input"] = (
            aws_sdk_glue.types.connection_input.deserialize_aws_json_1_1(
                data["ConnectionInput"]
            )
        )
    else:
        raise DeserializationError("CreateConnectionRequest.connection_input required")
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out

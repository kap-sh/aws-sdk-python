"""Generated from Smithy shape ``com.amazonaws.glue#UpdateConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.connection_input
    import aws_sdk_glue.types.name_string


class UpdateConnectionRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the connection definition to update.</p>"""
    connection_input: "aws_sdk_glue.types.connection_input.ConnectionInput"
    """<p>A <code>ConnectionInput</code> object that redefines the connection in question.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    import aws_sdk_glue.types.connection_input

    out["ConnectionInput"] = aws_sdk_glue.types.connection_input.serialize_aws_json_1_1(
        value["connection_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionRequest:
    out: UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateConnectionRequest.name required")
    if "ConnectionInput" in data:
        import aws_sdk_glue.types.connection_input

        out["connection_input"] = (
            aws_sdk_glue.types.connection_input.deserialize_aws_json_1_1(
                data["ConnectionInput"]
            )
        )
    else:
        raise DeserializationError("UpdateConnectionRequest.connection_input required")
    return out

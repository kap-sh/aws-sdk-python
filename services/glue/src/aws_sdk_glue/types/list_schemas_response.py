"""Generated from Smithy shape ``com.amazonaws.glue#ListSchemasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_list_definition
    import aws_sdk_glue.types.schema_registry_token_string


class ListSchemasResponse(TypedDict):
    schemas: NotRequired[
        "aws_sdk_glue.types.schema_list_definition.SchemaListDefinition"
    ]
    """<p>An array of <code>SchemaListItem</code> objects containing details of each schema.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasResponse) -> dict:
    out: dict = {}
    if "schemas" in value:
        import aws_sdk_glue.types.schema_list_definition

        out["Schemas"] = (
            aws_sdk_glue.types.schema_list_definition.serialize_aws_json_1_1(
                value["schemas"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasResponse:
    out: ListSchemasResponse = {}  # type: ignore[typeddict-item]
    if "Schemas" in data:
        import aws_sdk_glue.types.schema_list_definition

        out["schemas"] = (
            aws_sdk_glue.types.schema_list_definition.deserialize_aws_json_1_1(
                data["Schemas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

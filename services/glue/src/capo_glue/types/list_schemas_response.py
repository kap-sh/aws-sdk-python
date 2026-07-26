"""Generated from Smithy shape ``com.amazonaws.glue#ListSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.schema_list_definition
    import capo_glue.types.schema_registry_token_string


class ListSchemasResponse(TypedDict, closed=True):
    schemas: NotRequired["capo_glue.types.schema_list_definition.SchemaListDefinition"]
    """<p>An array of <code>SchemaListItem</code> objects containing details of each schema.</p>"""
    next_token: NotRequired[
        "capo_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasResponse) -> dict:
    out: dict = {}
    if "schemas" in value:
        import capo_glue.types.schema_list_definition

        out["Schemas"] = capo_glue.types.schema_list_definition.serialize_aws_json_1_1(
            value["schemas"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasResponse:
    out: ListSchemasResponse = {}  # type: ignore[typeddict-item]
    if "Schemas" in data:
        import capo_glue.types.schema_list_definition

        out["schemas"] = (
            capo_glue.types.schema_list_definition.deserialize_aws_json_1_1(
                data["Schemas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

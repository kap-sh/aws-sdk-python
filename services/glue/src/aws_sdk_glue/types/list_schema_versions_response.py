"""Generated from Smithy shape ``com.amazonaws.glue#ListSchemaVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.schema_registry_token_string
    import aws_sdk_glue.types.schema_version_list


class ListSchemaVersionsResponse(TypedDict, closed=True):
    schemas: NotRequired["aws_sdk_glue.types.schema_version_list.SchemaVersionList"]
    """<p>An array of <code>SchemaVersionList</code> objects containing details of each schema version.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.schema_registry_token_string.SchemaRegistryTokenString"
    ]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemaVersionsResponse) -> dict:
    out: dict = {}
    if "schemas" in value:
        import aws_sdk_glue.types.schema_version_list

        out["Schemas"] = aws_sdk_glue.types.schema_version_list.serialize_aws_json_1_1(
            value["schemas"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemaVersionsResponse:
    out: ListSchemaVersionsResponse = {}  # type: ignore[typeddict-item]
    if "Schemas" in data:
        import aws_sdk_glue.types.schema_version_list

        out["schemas"] = (
            aws_sdk_glue.types.schema_version_list.deserialize_aws_json_1_1(
                data["Schemas"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

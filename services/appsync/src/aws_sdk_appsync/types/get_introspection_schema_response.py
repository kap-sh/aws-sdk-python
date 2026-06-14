"""Generated from Smithy shape ``com.amazonaws.appsync#GetIntrospectionSchemaResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.blob


class GetIntrospectionSchemaResponse(TypedDict):
    schema: NotRequired["aws_sdk_appsync.types.blob.Blob"]
    r"""<p>The schema, in GraphQL Schema Definition Language (SDL) format.</p> <p>For more information, see the <a href=\"http://graphql.org/learn/schema/\">GraphQL SDL documentation</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntrospectionSchemaResponse) -> dict:
    out: dict = {}
    if "schema" in value:
        import aws_sdk_appsync.types.blob

        out["schema"] = aws_sdk_appsync.types.blob.serialize_json(value["schema"])
    return out


def deserialize_json(data: dict) -> GetIntrospectionSchemaResponse:
    out: GetIntrospectionSchemaResponse = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import aws_sdk_appsync.types.blob

        out["schema"] = aws_sdk_appsync.types.blob.deserialize_json(data["schema"])
    return out

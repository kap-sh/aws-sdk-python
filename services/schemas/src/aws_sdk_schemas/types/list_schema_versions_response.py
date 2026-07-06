"""Generated from Smithy shape ``com.amazonaws.schemas#ListSchemaVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__list_of_schema_version_summary
    import aws_sdk_schemas.types.__string


class ListSchemaVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""
    schema_versions: NotRequired[
        "aws_sdk_schemas.types.__list_of_schema_version_summary.__listOfSchemaVersionSummary"
    ]
    """<p>An array of schema version summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemaVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "schema_versions" in value:
        import aws_sdk_schemas.types.__list_of_schema_version_summary

        out["SchemaVersions"] = (
            aws_sdk_schemas.types.__list_of_schema_version_summary.serialize_json(
                value["schema_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSchemaVersionsResponse:
    out: ListSchemaVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SchemaVersions" in data:
        import aws_sdk_schemas.types.__list_of_schema_version_summary

        out["schema_versions"] = (
            aws_sdk_schemas.types.__list_of_schema_version_summary.deserialize_json(
                data["SchemaVersions"]
            )
        )
    return out

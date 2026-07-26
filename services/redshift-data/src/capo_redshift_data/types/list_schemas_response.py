"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_data.types.schema_list
    import capo_redshift_data.types.string


class ListSchemasResponse(TypedDict, closed=True):
    schemas: NotRequired["capo_redshift_data.types.schema_list.SchemaList"]
    """<p>The schemas that match the request pattern. </p>"""
    next_token: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasResponse) -> dict:
    out: dict = {}
    if "schemas" in value:
        import capo_redshift_data.types.schema_list

        out["Schemas"] = capo_redshift_data.types.schema_list.serialize_aws_json_1_1(
            value["schemas"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasResponse:
    out: ListSchemasResponse = {}  # type: ignore[typeddict-item]
    if "Schemas" in data:
        import capo_redshift_data.types.schema_list

        out["schemas"] = capo_redshift_data.types.schema_list.deserialize_aws_json_1_1(
            data["Schemas"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

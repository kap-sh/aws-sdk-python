"""Generated from Smithy shape ``com.amazonaws.athena#UpdateNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.named_query_description_string
    import aws_sdk_athena.types.named_query_id
    import aws_sdk_athena.types.query_string


class UpdateNamedQueryInput(TypedDict, closed=True):
    named_query_id: "aws_sdk_athena.types.named_query_id.NamedQueryId"
    """<p>The unique identifier (UUID) of the query.</p>"""
    name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The name of the query.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.named_query_description_string.NamedQueryDescriptionString"
    ]
    """<p>The query description.</p>"""
    query_string: "aws_sdk_athena.types.query_string.QueryString"
    """<p>The contents of the query with all query statements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNamedQueryInput) -> dict:
    out: dict = {}
    out["NamedQueryId"] = value["named_query_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["QueryString"] = value["query_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNamedQueryInput:
    out: UpdateNamedQueryInput = {}  # type: ignore[typeddict-item]
    if "NamedQueryId" in data:
        out["named_query_id"] = data["NamedQueryId"]
    else:
        raise DeserializationError("UpdateNamedQueryInput.named_query_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateNamedQueryInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("UpdateNamedQueryInput.query_string required")
    return out

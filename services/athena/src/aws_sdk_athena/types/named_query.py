"""Generated from Smithy shape ``com.amazonaws.athena#NamedQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.database_string
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.named_query_id
    import aws_sdk_athena.types.query_string
    import aws_sdk_athena.types.work_group_name


class NamedQuery(TypedDict):
    name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The query name.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>The query description.</p>"""
    database: "aws_sdk_athena.types.database_string.DatabaseString"
    """<p>The database to which the query belongs.</p>"""
    query_string: "aws_sdk_athena.types.query_string.QueryString"
    """<p>The SQL statements that make up the query.</p>"""
    named_query_id: NotRequired["aws_sdk_athena.types.named_query_id.NamedQueryId"]
    """<p>The unique identifier of the query.</p>"""
    work_group: NotRequired["aws_sdk_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup that contains the named query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamedQuery) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Database"] = value["database"]
    out["QueryString"] = value["query_string"]
    if "named_query_id" in value:
        out["NamedQueryId"] = value["named_query_id"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NamedQuery:
    out: NamedQuery = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("NamedQuery.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("NamedQuery.database required")
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("NamedQuery.query_string required")
    if "NamedQueryId" in data:
        out["named_query_id"] = data["NamedQueryId"]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    return out

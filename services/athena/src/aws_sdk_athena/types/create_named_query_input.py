"""Generated from Smithy shape ``com.amazonaws.athena#CreateNamedQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.database_string
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.idempotency_token
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.query_string
    import aws_sdk_athena.types.work_group_name


class CreateNamedQueryInput(TypedDict):
    name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The query name.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>The query description.</p>"""
    database: "aws_sdk_athena.types.database_string.DatabaseString"
    """<p>The database to which the query belongs.</p>"""
    query_string: "aws_sdk_athena.types.query_string.QueryString"
    """<p>The contents of the query with all query statements.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_athena.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another <code>CreateNamedQuery</code> request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the <code>QueryString</code>, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""
    work_group: NotRequired["aws_sdk_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup in which the named query is being created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamedQueryInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Database"] = value["database"]
    out["QueryString"] = value["query_string"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamedQueryInput:
    out: CreateNamedQueryInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateNamedQueryInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("CreateNamedQueryInput.database required")
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("CreateNamedQueryInput.query_string required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    return out

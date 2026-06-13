"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListDatabasesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.cluster_identifier_string
    import aws_sdk_redshift_data.types.page_size
    import aws_sdk_redshift_data.types.secret_arn
    import aws_sdk_redshift_data.types.string
    import aws_sdk_redshift_data.types.workgroup_name_string


class ListDatabasesRequest(TypedDict):
    cluster_identifier: NotRequired[
        "aws_sdk_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
    ]
    """<p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>"""
    database: "aws_sdk_redshift_data.types.string.String"
    """<p>The name of the database. This parameter is required when authenticating using either Secrets Manager or temporary credentials. </p>"""
    secret_arn: NotRequired["aws_sdk_redshift_data.types.secret_arn.SecretArn"]
    """<p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>"""
    db_user: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>"""
    next_token: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""
    max_results: "aws_sdk_redshift_data.types.page_size.PageSize"
    """<p>The maximum number of databases to return in the response. If more databases exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>"""
    workgroup_name: NotRequired[
        "aws_sdk_redshift_data.types.workgroup_name_string.WorkgroupNameString"
    ]
    """<p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatabasesRequest) -> dict:
    out: dict = {}
    if "cluster_identifier" in value:
        out["ClusterIdentifier"] = value["cluster_identifier"]
    out["Database"] = value["database"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value.get("max_results", 0)
    if "workgroup_name" in value:
        out["WorkgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatabasesRequest:
    out: ListDatabasesRequest = {}  # type: ignore[typeddict-item]
    if "ClusterIdentifier" in data:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("ListDatabasesRequest.database required")
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "DbUser" in data:
        out["db_user"] = data["DbUser"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "WorkgroupName" in data:
        out["workgroup_name"] = data["WorkgroupName"]
    return out

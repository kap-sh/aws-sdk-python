"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListStatementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.cluster_identifier_string
    import aws_sdk_redshift_data.types.list_statements_limit
    import aws_sdk_redshift_data.types.statement_name_string
    import aws_sdk_redshift_data.types.status_string
    import aws_sdk_redshift_data.types.string
    import aws_sdk_redshift_data.types.workgroup_name_string


class ListStatementsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""
    max_results: "aws_sdk_redshift_data.types.list_statements_limit.ListStatementsLimit"
    """<p>The maximum number of SQL statements to return in the response. If more SQL statements exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>"""
    statement_name: NotRequired[
        "aws_sdk_redshift_data.types.statement_name_string.StatementNameString"
    ]
    """<p>The name of the SQL statement specified as input to <code>BatchExecuteStatement</code> or <code>ExecuteStatement</code> to identify the query. You can list multiple statements by providing a prefix that matches the beginning of the statement name. For example, to list myStatement1, myStatement2, myStatement3, and so on, then provide the a value of <code>myStatement</code>. Data API does a case-sensitive match of SQL statement names to the prefix value you provide. </p>"""
    status: NotRequired["aws_sdk_redshift_data.types.status_string.StatusString"]
    """<p>The status of the SQL statement to list. Status values are defined as follows: </p> <ul> <li> <p>ABORTED - The query run was stopped by the user. </p> </li> <li> <p>ALL - A status value that includes all query statuses. This value can be used to filter results. </p> </li> <li> <p>FAILED - The query run failed. </p> </li> <li> <p>FINISHED - The query has finished running. </p> </li> <li> <p>PICKED - The query has been chosen to be run. </p> </li> <li> <p>STARTED - The query run has started. </p> </li> <li> <p>SUBMITTED - The query was submitted, but not yet processed. </p> </li> </ul>"""
    role_level: NotRequired["bool"]
    """<p>A value that filters which statements to return in the response. If true, all statements run by the caller's IAM role are returned. If false, only statements run by the caller's IAM role in the current IAM session are returned. The default is true. </p>"""
    database: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>The name of the database when listing statements run against a <code>ClusterIdentifier</code> or <code>WorkgroupName</code>. </p>"""
    cluster_identifier: NotRequired[
        "aws_sdk_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
    ]
    """<p>The cluster identifier. Only statements that ran on this cluster are returned. When providing <code>ClusterIdentifier</code>, then <code>WorkgroupName</code> can't be specified.</p>"""
    workgroup_name: NotRequired[
        "aws_sdk_redshift_data.types.workgroup_name_string.WorkgroupNameString"
    ]
    """<p>The serverless workgroup name or Amazon Resource Name (ARN). Only statements that ran on this workgroup are returned. When providing <code>WorkgroupName</code>, then <code>ClusterIdentifier</code> can't be specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value.get("max_results", 0)
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "role_level" in value:
        out["RoleLevel"] = value["role_level"]
    if "database" in value:
        out["Database"] = value["database"]
    if "cluster_identifier" in value:
        out["ClusterIdentifier"] = value["cluster_identifier"]
    if "workgroup_name" in value:
        out["WorkgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsRequest:
    out: ListStatementsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "RoleLevel" in data:
        out["role_level"] = data["RoleLevel"]
    if "Database" in data:
        out["database"] = data["Database"]
    if "ClusterIdentifier" in data:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    if "WorkgroupName" in data:
        out["workgroup_name"] = data["WorkgroupName"]
    return out

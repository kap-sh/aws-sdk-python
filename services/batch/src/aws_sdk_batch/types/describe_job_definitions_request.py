"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list


class DescribeJobDefinitionsRequest(TypedDict):
    job_definitions: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>A list of up to 100 job definitions. Each entry in the list can either be an ARN in the format <code>arn:aws:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision}</code> or a short version using the form <code>${JobDefinitionName}:${Revision}</code>. This parameter can't be used with other parameters.</p>"""
    max_results: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>DescribeJobDefinitions</code> in paginated output. When this parameter is used, <code>DescribeJobDefinitions</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeJobDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeJobDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    job_definition_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the job definition to describe.</p>"""
    status: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The status used to filter job definitions.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeJobDefinitions</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobDefinitionsRequest) -> dict:
    out: dict = {}
    if "job_definitions" in value:
        import aws_sdk_batch.types.string_list

        out["jobDefinitions"] = aws_sdk_batch.types.string_list.serialize_json(
            value["job_definitions"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "job_definition_name" in value:
        out["jobDefinitionName"] = value["job_definition_name"]
    if "status" in value:
        out["status"] = value["status"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobDefinitionsRequest:
    out: DescribeJobDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "jobDefinitions" in data:
        import aws_sdk_batch.types.string_list

        out["job_definitions"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["jobDefinitions"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "jobDefinitionName" in data:
        out["job_definition_name"] = data["jobDefinitionName"]
    if "status" in data:
        out["status"] = data["status"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

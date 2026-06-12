"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.job_definition_list
    import aws_sdk_batch.types.string


class DescribeJobDefinitionsResponse(TypedDict):
    job_definitions: NotRequired[
        "aws_sdk_batch.types.job_definition_list.JobDefinitionList"
    ]
    """<p>The list of job definitions.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeJobDefinitions</code> request. When the results of a <code>DescribeJobDefinitions</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobDefinitionsResponse) -> dict:
    out: dict = {}
    if "job_definitions" in value:
        import aws_sdk_batch.types.job_definition_list

        out["jobDefinitions"] = aws_sdk_batch.types.job_definition_list.serialize_json(
            value["job_definitions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobDefinitionsResponse:
    out: DescribeJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "jobDefinitions" in data:
        import aws_sdk_batch.types.job_definition_list

        out["job_definitions"] = (
            aws_sdk_batch.types.job_definition_list.deserialize_json(
                data["jobDefinitions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

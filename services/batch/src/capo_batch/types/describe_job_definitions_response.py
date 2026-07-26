"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.job_definition_list
    import capo_batch.types.string


class DescribeJobDefinitionsResponse(TypedDict, closed=True):
    job_definitions: NotRequired[
        "capo_batch.types.job_definition_list.JobDefinitionList"
    ]
    """<p>The list of job definitions.</p>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeJobDefinitions</code> request. When the results of a <code>DescribeJobDefinitions</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobDefinitionsResponse) -> dict:
    out: dict = {}
    if "job_definitions" in value:
        import capo_batch.types.job_definition_list

        out["jobDefinitions"] = capo_batch.types.job_definition_list.serialize_json(
            value["job_definitions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobDefinitionsResponse:
    out: DescribeJobDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "jobDefinitions" in data:
        import capo_batch.types.job_definition_list

        out["job_definitions"] = capo_batch.types.job_definition_list.deserialize_json(
            data["jobDefinitions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

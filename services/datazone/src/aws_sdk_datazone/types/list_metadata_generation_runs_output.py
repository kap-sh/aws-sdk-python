"""Generated from Smithy shape ``com.amazonaws.datazone#ListMetadataGenerationRunsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.metadata_generation_runs
    import aws_sdk_datazone.types.pagination_token


class ListMetadataGenerationRunsOutput(TypedDict):
    items: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_runs.MetadataGenerationRuns"
    ]
    """<p>The results of the ListMetadataGenerationRuns action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataGenerationRunsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.metadata_generation_runs

        out["items"] = aws_sdk_datazone.types.metadata_generation_runs.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMetadataGenerationRunsOutput:
    out: ListMetadataGenerationRunsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.metadata_generation_runs

        out["items"] = aws_sdk_datazone.types.metadata_generation_runs.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

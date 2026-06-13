"""Generated from Smithy shape ``com.amazonaws.datazone#ListMetadataGenerationRunsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.metadata_generation_run_status
    import aws_sdk_datazone.types.metadata_generation_run_type
    import aws_sdk_datazone.types.pagination_token


class ListMetadataGenerationRunsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where you want to list metadata generation runs.</p>"""
    status: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
    ]
    """<p>The status of the metadata generation runs.</p>"""
    type: NotRequired[
        "aws_sdk_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    ]
    """<p>The type of the metadata generation runs.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>"""
    target_identifier: NotRequired["aws_sdk_datazone.types.entity_id.EntityId"]
    """<p>The target ID for which you want to list metadata generation runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataGenerationRunsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMetadataGenerationRunsInput:
    out: ListMetadataGenerationRunsInput = {}  # type: ignore[typeddict-item]
    return out

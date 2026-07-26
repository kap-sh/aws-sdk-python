"""Generated from Smithy shape ``com.amazonaws.healthlake#ListFHIRDatastoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_filter
    import capo_healthlake.types.max_results_integer
    import capo_healthlake.types.next_token


class ListFHIRDatastoresRequest(TypedDict, closed=True):
    filter: NotRequired["capo_healthlake.types.datastore_filter.DatastoreFilter"]
    """<p>List all filters associated with a FHIR data store request.</p>"""
    next_token: NotRequired["capo_healthlake.types.next_token.NextToken"]
    """<p>The token used to retrieve the next page of data stores when results are paginated.</p>"""
    max_results: NotRequired[
        "capo_healthlake.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of data stores returned on a page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFHIRDatastoresRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_healthlake.types.datastore_filter

        out["Filter"] = capo_healthlake.types.datastore_filter.serialize_aws_json_1_0(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFHIRDatastoresRequest:
    out: ListFHIRDatastoresRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import capo_healthlake.types.datastore_filter

        out["filter"] = capo_healthlake.types.datastore_filter.deserialize_aws_json_1_0(
            data["Filter"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out

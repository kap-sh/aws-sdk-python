"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchImageSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.next_token
    import aws_sdk_medical_imaging.types.search_criteria


class SearchImageSetsRequest(TypedDict):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The identifier of the data store where the image sets reside.</p>"""
    search_criteria: NotRequired[
        "aws_sdk_medical_imaging.types.search_criteria.SearchCriteria"
    ]
    """<p>The search criteria that filters by applying a maximum of 1 item to <code>SearchByAttribute</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that can be returned in a search.</p>"""
    next_token: NotRequired["aws_sdk_medical_imaging.types.next_token.NextToken"]
    """<p>The token used for pagination of results returned in the response. Use the token returned from the previous request to continue results where the previous request ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchImageSetsRequest) -> dict:
    out: dict = {}
    if "search_criteria" in value:
        import aws_sdk_medical_imaging.types.search_criteria

        out["searchCriteria"] = (
            aws_sdk_medical_imaging.types.search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchImageSetsRequest:
    out: SearchImageSetsRequest = {}  # type: ignore[typeddict-item]
    if "searchCriteria" in data:
        import aws_sdk_medical_imaging.types.search_criteria

        out["search_criteria"] = (
            aws_sdk_medical_imaging.types.search_criteria.deserialize_json(
                data["searchCriteria"]
            )
        )
    return out

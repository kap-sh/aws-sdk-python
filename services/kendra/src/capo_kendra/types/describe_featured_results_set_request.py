"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeFeaturedResultsSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set_id
    import capo_kendra.types.index_id


class DescribeFeaturedResultsSetRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used for featuring results.</p>"""
    featured_results_set_id: (
        "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    )
    """<p>The identifier of the set of featured results that you want to get information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeaturedResultsSetRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["FeaturedResultsSetId"] = value["featured_results_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeaturedResultsSetRequest:
    out: DescribeFeaturedResultsSetRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "DescribeFeaturedResultsSetRequest.index_id required"
        )
    if "FeaturedResultsSetId" in data:
        out["featured_results_set_id"] = data["FeaturedResultsSetId"]
    else:
        raise DeserializationError(
            "DescribeFeaturedResultsSetRequest.featured_results_set_id required"
        )
    return out

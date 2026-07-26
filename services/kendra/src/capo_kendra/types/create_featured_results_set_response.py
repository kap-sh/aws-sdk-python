"""Generated from Smithy shape ``com.amazonaws.kendra#CreateFeaturedResultsSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.featured_results_set


class CreateFeaturedResultsSetResponse(TypedDict, closed=True):
    featured_results_set: NotRequired[
        "capo_kendra.types.featured_results_set.FeaturedResultsSet"
    ]
    """<p>Information on the set of featured results. This includes the identifier of the featured results set, whether the featured results set is active or inactive, when the featured results set was created, and more.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFeaturedResultsSetResponse) -> dict:
    out: dict = {}
    if "featured_results_set" in value:
        import capo_kendra.types.featured_results_set

        out["FeaturedResultsSet"] = (
            capo_kendra.types.featured_results_set.serialize_aws_json_1_1(
                value["featured_results_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFeaturedResultsSetResponse:
    out: CreateFeaturedResultsSetResponse = {}  # type: ignore[typeddict-item]
    if "FeaturedResultsSet" in data:
        import capo_kendra.types.featured_results_set

        out["featured_results_set"] = (
            capo_kendra.types.featured_results_set.deserialize_aws_json_1_1(
                data["FeaturedResultsSet"]
            )
        )
    return out

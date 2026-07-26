"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_schema_summary_list
    import capo_customer_profiles.types.token


class ListRecommenderSchemasResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommender_schemas: NotRequired[
        "capo_customer_profiles.types.recommender_schema_summary_list.RecommenderSchemaSummaryList"
    ]
    """<p>A list of recommender schemas and their properties in the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderSchemasResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommender_schemas" in value:
        import capo_customer_profiles.types.recommender_schema_summary_list

        out["RecommenderSchemas"] = (
            capo_customer_profiles.types.recommender_schema_summary_list.serialize_json(
                value["recommender_schemas"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommenderSchemasResponse:
    out: ListRecommenderSchemasResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecommenderSchemas" in data:
        import capo_customer_profiles.types.recommender_schema_summary_list

        out["recommender_schemas"] = (
            capo_customer_profiles.types.recommender_schema_summary_list.deserialize_json(
                data["RecommenderSchemas"]
            )
        )
    return out

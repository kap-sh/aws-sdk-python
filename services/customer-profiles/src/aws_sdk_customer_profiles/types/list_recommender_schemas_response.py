"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderSchemasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_schema_summary_list
    import aws_sdk_customer_profiles.types.token


class ListRecommenderSchemasResponse(TypedDict):
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommender_schemas: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_schema_summary_list.RecommenderSchemaSummaryList"
    ]
    """<p>A list of recommender schemas and their properties in the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderSchemasResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommender_schemas" in value:
        import aws_sdk_customer_profiles.types.recommender_schema_summary_list

        out["RecommenderSchemas"] = (
            aws_sdk_customer_profiles.types.recommender_schema_summary_list.serialize_json(
                value["recommender_schemas"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommenderSchemasResponse:
    out: ListRecommenderSchemasResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecommenderSchemas" in data:
        import aws_sdk_customer_profiles.types.recommender_schema_summary_list

        out["recommender_schemas"] = (
            aws_sdk_customer_profiles.types.recommender_schema_summary_list.deserialize_json(
                data["RecommenderSchemas"]
            )
        )
    return out

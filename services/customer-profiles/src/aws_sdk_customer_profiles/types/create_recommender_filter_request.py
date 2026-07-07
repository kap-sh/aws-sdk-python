"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_filter_expression
    import aws_sdk_customer_profiles.types.recommender_filter_name
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.tag_map


class CreateRecommenderFilterRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_filter_name: (
        "aws_sdk_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    )
    """<p>The name of the recommender filter. The name must be unique within the domain.</p>"""
    recommender_filter_expression: "aws_sdk_customer_profiles.types.recommender_filter_expression.RecommenderFilterExpression"
    """<p>The filter expression that defines which items to include or exclude from recommendations.</p>"""
    recommender_schema_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema to use for this recommender filter. If not specified, the default schema is used.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>A description of the recommender filter.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderFilterRequest) -> dict:
    out: dict = {}
    out["RecommenderFilterExpression"] = value["recommender_filter_expression"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRecommenderFilterRequest:
    out: CreateRecommenderFilterRequest = {}  # type: ignore[typeddict-item]
    if "RecommenderFilterExpression" in data:
        out["recommender_filter_expression"] = data["RecommenderFilterExpression"]
    else:
        raise DeserializationError(
            "CreateRecommenderFilterRequest.recommender_filter_expression required"
        )
    if "RecommenderSchemaName" in data:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out

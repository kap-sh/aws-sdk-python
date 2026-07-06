"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_config
    import aws_sdk_customer_profiles.types.recommender_recipe_name
    import aws_sdk_customer_profiles.types.sensitive_text
    import aws_sdk_customer_profiles.types.tag_map


class CreateRecommenderRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender.</p>"""
    recommender_recipe_name: (
        "aws_sdk_customer_profiles.types.recommender_recipe_name.RecommenderRecipeName"
    )
    """<p>The name of the recommeder recipe.</p>"""
    recommender_config: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_config.RecommenderConfig"
    ]
    """<p>The recommender configuration.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the domain object type.</p>"""
    recommender_schema_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>The name of the recommender schema to use for this recommender. If not specified, the default schema is used.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.recommender_recipe_name

    out["RecommenderRecipeName"] = (
        aws_sdk_customer_profiles.types.recommender_recipe_name.serialize_json(
            value["recommender_recipe_name"]
        )
    )
    if "recommender_config" in value:
        import aws_sdk_customer_profiles.types.recommender_config

        out["RecommenderConfig"] = (
            aws_sdk_customer_profiles.types.recommender_config.serialize_json(
                value["recommender_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "recommender_schema_name" in value:
        out["RecommenderSchemaName"] = value["recommender_schema_name"]
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRecommenderRequest:
    out: CreateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if "RecommenderRecipeName" in data:
        import aws_sdk_customer_profiles.types.recommender_recipe_name

        out["recommender_recipe_name"] = (
            aws_sdk_customer_profiles.types.recommender_recipe_name.deserialize_json(
                data["RecommenderRecipeName"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRecommenderRequest.recommender_recipe_name required"
        )
    if "RecommenderConfig" in data:
        import aws_sdk_customer_profiles.types.recommender_config

        out["recommender_config"] = (
            aws_sdk_customer_profiles.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RecommenderSchemaName" in data:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out

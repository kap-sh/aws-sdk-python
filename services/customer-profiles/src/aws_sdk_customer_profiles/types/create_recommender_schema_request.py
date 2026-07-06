"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_schema_fields
    import aws_sdk_customer_profiles.types.tag_map


class CreateRecommenderSchemaRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_schema_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender schema. The name must be unique within the domain.</p>"""
    fields: "aws_sdk_customer_profiles.types.recommender_schema_fields.RecommenderSchemaFields"
    """<p>A map of dataset type to column definitions that specifies which data columns to include in the schema. The <code>_webAnalytics</code> and <code>_catalogItem</code> keys are supported.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderSchemaRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.recommender_schema_fields

    out["Fields"] = (
        aws_sdk_customer_profiles.types.recommender_schema_fields.serialize_json(
            value["fields"]
        )
    )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRecommenderSchemaRequest:
    out: CreateRecommenderSchemaRequest = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_customer_profiles.types.recommender_schema_fields

        out["fields"] = (
            aws_sdk_customer_profiles.types.recommender_schema_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("CreateRecommenderSchemaRequest.fields required")
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.arn
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_schema_fields
    import capo_customer_profiles.types.recommender_schema_status
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp


class CreateRecommenderSchemaResponse(TypedDict, closed=True):
    recommender_schema_arn: "capo_customer_profiles.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender schema.</p>"""
    recommender_schema_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender schema.</p>"""
    fields: (
        "capo_customer_profiles.types.recommender_schema_fields.RecommenderSchemaFields"
    )
    """<p>A map of dataset type to column definitions included in the schema.</p>"""
    created_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp of when the recommender schema was created.</p>"""
    status: (
        "capo_customer_profiles.types.recommender_schema_status.RecommenderSchemaStatus"
    )
    """<p>The status of the recommender schema.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderSchemaResponse) -> dict:
    out: dict = {}
    out["RecommenderSchemaArn"] = value["recommender_schema_arn"]
    out["RecommenderSchemaName"] = value["recommender_schema_name"]
    import capo_customer_profiles.types.recommender_schema_fields

    out["Fields"] = (
        capo_customer_profiles.types.recommender_schema_fields.serialize_json(
            value["fields"]
        )
    )
    import capo_customer_profiles.types.timestamp

    out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_customer_profiles.types.recommender_schema_status

    out["Status"] = (
        capo_customer_profiles.types.recommender_schema_status.serialize_json(
            value["status"]
        )
    )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecommenderSchemaResponse:
    out: CreateRecommenderSchemaResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderSchemaArn" in data:
        out["recommender_schema_arn"] = data["RecommenderSchemaArn"]
    else:
        raise DeserializationError(
            "CreateRecommenderSchemaResponse.recommender_schema_arn required"
        )
    if "RecommenderSchemaName" in data:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    else:
        raise DeserializationError(
            "CreateRecommenderSchemaResponse.recommender_schema_name required"
        )
    if "Fields" in data:
        import capo_customer_profiles.types.recommender_schema_fields

        out["fields"] = (
            capo_customer_profiles.types.recommender_schema_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("CreateRecommenderSchemaResponse.fields required")
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError(
            "CreateRecommenderSchemaResponse.created_at required"
        )
    if "Status" in data:
        import capo_customer_profiles.types.recommender_schema_status

        out["status"] = (
            capo_customer_profiles.types.recommender_schema_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CreateRecommenderSchemaResponse.status required")
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out

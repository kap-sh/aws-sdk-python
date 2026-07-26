"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetRecommenderSchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_schema_fields
    import capo_customer_profiles.types.recommender_schema_status
    import capo_customer_profiles.types.timestamp


class GetRecommenderSchemaResponse(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommenderSchemaResponse) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> GetRecommenderSchemaResponse:
    out: GetRecommenderSchemaResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderSchemaName" in data:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    else:
        raise DeserializationError(
            "GetRecommenderSchemaResponse.recommender_schema_name required"
        )
    if "Fields" in data:
        import capo_customer_profiles.types.recommender_schema_fields

        out["fields"] = (
            capo_customer_profiles.types.recommender_schema_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("GetRecommenderSchemaResponse.fields required")
    if "CreatedAt" in data:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("GetRecommenderSchemaResponse.created_at required")
    if "Status" in data:
        import capo_customer_profiles.types.recommender_schema_status

        out["status"] = (
            capo_customer_profiles.types.recommender_schema_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("GetRecommenderSchemaResponse.status required")
    return out

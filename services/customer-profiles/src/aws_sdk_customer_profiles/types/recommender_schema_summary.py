"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_schema_fields
    import aws_sdk_customer_profiles.types.recommender_schema_status
    import aws_sdk_customer_profiles.types.timestamp


class RecommenderSchemaSummary(TypedDict, closed=True):
    recommender_schema_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender schema.</p>"""
    fields: "aws_sdk_customer_profiles.types.recommender_schema_fields.RecommenderSchemaFields"
    """<p>A map of dataset type to column definitions included in the schema.</p>"""
    created_at: "aws_sdk_customer_profiles.types.timestamp.timestamp"
    """<p>The timestamp when the recommender schema was created.</p>"""
    status: "aws_sdk_customer_profiles.types.recommender_schema_status.RecommenderSchemaStatus"
    """<p>The current operational status of the recommender schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSchemaSummary) -> dict:
    out: dict = {}
    out["RecommenderSchemaName"] = value["recommender_schema_name"]
    import aws_sdk_customer_profiles.types.recommender_schema_fields

    out["Fields"] = (
        aws_sdk_customer_profiles.types.recommender_schema_fields.serialize_json(
            value["fields"]
        )
    )
    import aws_sdk_customer_profiles.types.timestamp

    out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_customer_profiles.types.recommender_schema_status

    out["Status"] = (
        aws_sdk_customer_profiles.types.recommender_schema_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecommenderSchemaSummary:
    out: RecommenderSchemaSummary = {}  # type: ignore[typeddict-item]
    if "RecommenderSchemaName" in data:
        out["recommender_schema_name"] = data["RecommenderSchemaName"]
    else:
        raise DeserializationError(
            "RecommenderSchemaSummary.recommender_schema_name required"
        )
    if "Fields" in data:
        import aws_sdk_customer_profiles.types.recommender_schema_fields

        out["fields"] = (
            aws_sdk_customer_profiles.types.recommender_schema_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("RecommenderSchemaSummary.fields required")
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("RecommenderSchemaSummary.created_at required")
    if "Status" in data:
        import aws_sdk_customer_profiles.types.recommender_schema_status

        out["status"] = (
            aws_sdk_customer_profiles.types.recommender_schema_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("RecommenderSchemaSummary.status required")
    return out

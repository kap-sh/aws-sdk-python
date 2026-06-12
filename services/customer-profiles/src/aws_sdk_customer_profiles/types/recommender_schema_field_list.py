"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.recommender_schema_field

RecommenderSchemaFieldList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.recommender_schema_field.RecommenderSchemaField"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSchemaFieldList) -> list:
    import aws_sdk_customer_profiles.types.recommender_schema_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.recommender_schema_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommenderSchemaFieldList:
    import aws_sdk_customer_profiles.types.recommender_schema_field

    out: RecommenderSchemaFieldList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.recommender_schema_field.deserialize_json(
                item
            )
        )
    return out

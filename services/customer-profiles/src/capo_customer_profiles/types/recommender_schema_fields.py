"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_schema_field_list

RecommenderSchemaFields: TypeAlias = dict[
    "str",
    "capo_customer_profiles.types.recommender_schema_field_list.RecommenderSchemaFieldList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RecommenderSchemaFields) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_customer_profiles.types.recommender_schema_field_list

        out[key] = (
            capo_customer_profiles.types.recommender_schema_field_list.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> RecommenderSchemaFields:
    out: RecommenderSchemaFields = {}
    for key, value in data.items():
        import capo_customer_profiles.types.recommender_schema_field_list

        out[key] = (
            capo_customer_profiles.types.recommender_schema_field_list.deserialize_json(
                value
            )
        )
    return out

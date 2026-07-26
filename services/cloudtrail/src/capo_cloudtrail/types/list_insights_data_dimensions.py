"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.list_insights_data_dimension_key
    import capo_cloudtrail.types.list_insights_data_dimension_value

ListInsightsDataDimensions: TypeAlias = dict[
    "capo_cloudtrail.types.list_insights_data_dimension_key.ListInsightsDataDimensionKey",
    "capo_cloudtrail.types.list_insights_data_dimension_value.ListInsightsDataDimensionValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ListInsightsDataDimensions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cloudtrail.types.list_insights_data_dimension_key

        out[
            capo_cloudtrail.types.list_insights_data_dimension_key.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInsightsDataDimensions:
    out: ListInsightsDataDimensions = {}
    for key, value in data.items():
        import capo_cloudtrail.types.list_insights_data_dimension_key

        out[
            capo_cloudtrail.types.list_insights_data_dimension_key.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out

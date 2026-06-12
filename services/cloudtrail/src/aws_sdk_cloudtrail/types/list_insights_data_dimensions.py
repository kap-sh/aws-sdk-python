"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsDataDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.list_insights_data_dimension_key
    import aws_sdk_cloudtrail.types.list_insights_data_dimension_value

ListInsightsDataDimensions: TypeAlias = dict[
    "aws_sdk_cloudtrail.types.list_insights_data_dimension_key.ListInsightsDataDimensionKey",
    "aws_sdk_cloudtrail.types.list_insights_data_dimension_value.ListInsightsDataDimensionValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ListInsightsDataDimensions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_cloudtrail.types.list_insights_data_dimension_key

        out[
            aws_sdk_cloudtrail.types.list_insights_data_dimension_key.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInsightsDataDimensions:
    out: ListInsightsDataDimensions = {}
    for key, value in data.items():
        import aws_sdk_cloudtrail.types.list_insights_data_dimension_key

        out[
            aws_sdk_cloudtrail.types.list_insights_data_dimension_key.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out

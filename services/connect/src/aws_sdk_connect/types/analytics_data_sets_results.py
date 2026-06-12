"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsDataSetsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.analytics_data_sets_result

AnalyticsDataSetsResults: TypeAlias = list[
    "aws_sdk_connect.types.analytics_data_sets_result.AnalyticsDataSetsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsDataSetsResults) -> list:
    import aws_sdk_connect.types.analytics_data_sets_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.analytics_data_sets_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsDataSetsResults:
    import aws_sdk_connect.types.analytics_data_sets_result

    out: AnalyticsDataSetsResults = []
    for item in data:
        out.append(
            aws_sdk_connect.types.analytics_data_sets_result.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsDataSetsResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.analytics_data_sets_result

AnalyticsDataSetsResults: TypeAlias = list[
    "capo_connect.types.analytics_data_sets_result.AnalyticsDataSetsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsDataSetsResults) -> list:
    import capo_connect.types.analytics_data_sets_result

    out: list = []
    for item in value:
        out.append(capo_connect.types.analytics_data_sets_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalyticsDataSetsResults:
    import capo_connect.types.analytics_data_sets_result

    out: AnalyticsDataSetsResults = []
    for item in data:
        out.append(capo_connect.types.analytics_data_sets_result.deserialize_json(item))
    return out

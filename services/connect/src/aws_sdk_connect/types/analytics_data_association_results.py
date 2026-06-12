"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsDataAssociationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.analytics_data_association_result

AnalyticsDataAssociationResults: TypeAlias = list[
    "aws_sdk_connect.types.analytics_data_association_result.AnalyticsDataAssociationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsDataAssociationResults) -> list:
    import aws_sdk_connect.types.analytics_data_association_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.analytics_data_association_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyticsDataAssociationResults:
    import aws_sdk_connect.types.analytics_data_association_result

    out: AnalyticsDataAssociationResults = []
    for item in data:
        out.append(
            aws_sdk_connect.types.analytics_data_association_result.deserialize_json(
                item
            )
        )
    return out

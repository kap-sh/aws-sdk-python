"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsReferenceDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_reference_data

PerformanceInsightsReferenceDataList: TypeAlias = list[
    "aws_sdk_devops_guru.types.performance_insights_reference_data.PerformanceInsightsReferenceData"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsReferenceDataList) -> list:
    import aws_sdk_devops_guru.types.performance_insights_reference_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.performance_insights_reference_data.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PerformanceInsightsReferenceDataList:
    import aws_sdk_devops_guru.types.performance_insights_reference_data

    out: PerformanceInsightsReferenceDataList = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.performance_insights_reference_data.deserialize_json(
                item
            )
        )
    return out

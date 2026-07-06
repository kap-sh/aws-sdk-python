"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#TemporalStatisticsConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.group_by
    import aws_sdk_sagemaker_geospatial.types.string_list_input
    import aws_sdk_sagemaker_geospatial.types.temporal_statistics_list_input


class TemporalStatisticsConfigInput(TypedDict, closed=True):
    group_by: NotRequired["aws_sdk_sagemaker_geospatial.types.group_by.GroupBy"]
    """<p>The input for the temporal statistics grouping by time frequency option.</p>"""
    statistics: "aws_sdk_sagemaker_geospatial.types.temporal_statistics_list_input.TemporalStatisticsListInput"
    """<p>The list of the statistics method options.</p>"""
    target_bands: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>The list of target band names for the temporal statistic to calculate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemporalStatisticsConfigInput) -> dict:
    out: dict = {}
    if "group_by" in value:
        out["GroupBy"] = value["group_by"]
    import aws_sdk_sagemaker_geospatial.types.temporal_statistics_list_input

    out["Statistics"] = (
        aws_sdk_sagemaker_geospatial.types.temporal_statistics_list_input.serialize_json(
            value["statistics"]
        )
    )
    if "target_bands" in value:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["TargetBands"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["target_bands"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemporalStatisticsConfigInput:
    out: TemporalStatisticsConfigInput = {}  # type: ignore[typeddict-item]
    if "GroupBy" in data:
        out["group_by"] = data["GroupBy"]
    if "Statistics" in data:
        import aws_sdk_sagemaker_geospatial.types.temporal_statistics_list_input

        out["statistics"] = (
            aws_sdk_sagemaker_geospatial.types.temporal_statistics_list_input.deserialize_json(
                data["Statistics"]
            )
        )
    else:
        raise DeserializationError("TemporalStatisticsConfigInput.statistics required")
    if "TargetBands" in data:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["target_bands"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["TargetBands"]
            )
        )
    return out

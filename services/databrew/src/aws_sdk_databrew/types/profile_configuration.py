"""Generated from Smithy shape ``com.amazonaws.databrew#ProfileConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.column_selector_list
    import aws_sdk_databrew.types.column_statistics_configuration_list
    import aws_sdk_databrew.types.entity_detector_configuration
    import aws_sdk_databrew.types.statistics_configuration


class ProfileConfiguration(TypedDict, closed=True):
    dataset_statistics_configuration: NotRequired[
        "aws_sdk_databrew.types.statistics_configuration.StatisticsConfiguration"
    ]
    """<p>Configuration for inter-column evaluations. Configuration can be used to select evaluations and override parameters of evaluations. When configuration is undefined, the profile job will run all supported inter-column evaluations. </p>"""
    profile_columns: NotRequired[
        "aws_sdk_databrew.types.column_selector_list.ColumnSelectorList"
    ]
    """<p>List of column selectors. ProfileColumns can be used to select columns from the dataset. When ProfileColumns is undefined, the profile job will profile all supported columns. </p>"""
    column_statistics_configurations: NotRequired[
        "aws_sdk_databrew.types.column_statistics_configuration_list.ColumnStatisticsConfigurationList"
    ]
    """<p>List of configurations for column evaluations. ColumnStatisticsConfigurations are used to select evaluations and override parameters of evaluations for particular columns. When ColumnStatisticsConfigurations is undefined, the profile job will profile all supported columns and run all supported evaluations. </p>"""
    entity_detector_configuration: NotRequired[
        "aws_sdk_databrew.types.entity_detector_configuration.EntityDetectorConfiguration"
    ]
    """<p>Configuration of entity detection for a profile job. When undefined, entity detection is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileConfiguration) -> dict:
    out: dict = {}
    if "dataset_statistics_configuration" in value:
        import aws_sdk_databrew.types.statistics_configuration

        out["DatasetStatisticsConfiguration"] = (
            aws_sdk_databrew.types.statistics_configuration.serialize_json(
                value["dataset_statistics_configuration"]
            )
        )
    if "profile_columns" in value:
        import aws_sdk_databrew.types.column_selector_list

        out["ProfileColumns"] = (
            aws_sdk_databrew.types.column_selector_list.serialize_json(
                value["profile_columns"]
            )
        )
    if "column_statistics_configurations" in value:
        import aws_sdk_databrew.types.column_statistics_configuration_list

        out["ColumnStatisticsConfigurations"] = (
            aws_sdk_databrew.types.column_statistics_configuration_list.serialize_json(
                value["column_statistics_configurations"]
            )
        )
    if "entity_detector_configuration" in value:
        import aws_sdk_databrew.types.entity_detector_configuration

        out["EntityDetectorConfiguration"] = (
            aws_sdk_databrew.types.entity_detector_configuration.serialize_json(
                value["entity_detector_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileConfiguration:
    out: ProfileConfiguration = {}  # type: ignore[typeddict-item]
    if "DatasetStatisticsConfiguration" in data:
        import aws_sdk_databrew.types.statistics_configuration

        out["dataset_statistics_configuration"] = (
            aws_sdk_databrew.types.statistics_configuration.deserialize_json(
                data["DatasetStatisticsConfiguration"]
            )
        )
    if "ProfileColumns" in data:
        import aws_sdk_databrew.types.column_selector_list

        out["profile_columns"] = (
            aws_sdk_databrew.types.column_selector_list.deserialize_json(
                data["ProfileColumns"]
            )
        )
    if "ColumnStatisticsConfigurations" in data:
        import aws_sdk_databrew.types.column_statistics_configuration_list

        out["column_statistics_configurations"] = (
            aws_sdk_databrew.types.column_statistics_configuration_list.deserialize_json(
                data["ColumnStatisticsConfigurations"]
            )
        )
    if "EntityDetectorConfiguration" in data:
        import aws_sdk_databrew.types.entity_detector_configuration

        out["entity_detector_configuration"] = (
            aws_sdk_databrew.types.entity_detector_configuration.deserialize_json(
                data["EntityDetectorConfiguration"]
            )
        )
    return out

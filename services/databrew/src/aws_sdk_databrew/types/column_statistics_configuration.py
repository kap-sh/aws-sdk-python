"""Generated from Smithy shape ``com.amazonaws.databrew#ColumnStatisticsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.column_selector_list
    import aws_sdk_databrew.types.statistics_configuration


class ColumnStatisticsConfiguration(TypedDict, closed=True):
    selectors: NotRequired[
        "aws_sdk_databrew.types.column_selector_list.ColumnSelectorList"
    ]
    """<p>List of column selectors. Selectors can be used to select columns from the dataset. When selectors are undefined, configuration will be applied to all supported columns. </p>"""
    statistics: (
        "aws_sdk_databrew.types.statistics_configuration.StatisticsConfiguration"
    )
    """<p>Configuration for evaluations. Statistics can be used to select evaluations and override parameters of evaluations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnStatisticsConfiguration) -> dict:
    out: dict = {}
    if "selectors" in value:
        import aws_sdk_databrew.types.column_selector_list

        out["Selectors"] = aws_sdk_databrew.types.column_selector_list.serialize_json(
            value["selectors"]
        )
    import aws_sdk_databrew.types.statistics_configuration

    out["Statistics"] = aws_sdk_databrew.types.statistics_configuration.serialize_json(
        value["statistics"]
    )
    return out


def deserialize_json(data: dict) -> ColumnStatisticsConfiguration:
    out: ColumnStatisticsConfiguration = {}  # type: ignore[typeddict-item]
    if "Selectors" in data:
        import aws_sdk_databrew.types.column_selector_list

        out["selectors"] = aws_sdk_databrew.types.column_selector_list.deserialize_json(
            data["Selectors"]
        )
    if "Statistics" in data:
        import aws_sdk_databrew.types.statistics_configuration

        out["statistics"] = (
            aws_sdk_databrew.types.statistics_configuration.deserialize_json(
                data["Statistics"]
            )
        )
    else:
        raise DeserializationError("ColumnStatisticsConfiguration.statistics required")
    return out

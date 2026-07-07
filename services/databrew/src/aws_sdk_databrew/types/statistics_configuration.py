"""Generated from Smithy shape ``com.amazonaws.databrew#StatisticsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.statistic_list
    import aws_sdk_databrew.types.statistic_override_list


class StatisticsConfiguration(TypedDict, closed=True):
    included_statistics: NotRequired[
        "aws_sdk_databrew.types.statistic_list.StatisticList"
    ]
    """<p>List of included evaluations. When the list is undefined, all supported evaluations will be included.</p>"""
    overrides: NotRequired[
        "aws_sdk_databrew.types.statistic_override_list.StatisticOverrideList"
    ]
    """<p>List of overrides for evaluations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticsConfiguration) -> dict:
    out: dict = {}
    if "included_statistics" in value:
        import aws_sdk_databrew.types.statistic_list

        out["IncludedStatistics"] = (
            aws_sdk_databrew.types.statistic_list.serialize_json(
                value["included_statistics"]
            )
        )
    if "overrides" in value:
        import aws_sdk_databrew.types.statistic_override_list

        out["Overrides"] = (
            aws_sdk_databrew.types.statistic_override_list.serialize_json(
                value["overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> StatisticsConfiguration:
    out: StatisticsConfiguration = {}  # type: ignore[typeddict-item]
    if "IncludedStatistics" in data:
        import aws_sdk_databrew.types.statistic_list

        out["included_statistics"] = (
            aws_sdk_databrew.types.statistic_list.deserialize_json(
                data["IncludedStatistics"]
            )
        )
    if "Overrides" in data:
        import aws_sdk_databrew.types.statistic_override_list

        out["overrides"] = (
            aws_sdk_databrew.types.statistic_override_list.deserialize_json(
                data["Overrides"]
            )
        )
    return out

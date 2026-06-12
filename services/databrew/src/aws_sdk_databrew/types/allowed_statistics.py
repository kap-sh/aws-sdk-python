"""Generated from Smithy shape ``com.amazonaws.databrew#AllowedStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.statistic_list


class AllowedStatistics(TypedDict):
    statistics: "aws_sdk_databrew.types.statistic_list.StatisticList"
    """<p>One or more column statistics to allow for columns that contain detected entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStatistics) -> dict:
    out: dict = {}
    import aws_sdk_databrew.types.statistic_list

    out["Statistics"] = aws_sdk_databrew.types.statistic_list.serialize_json(
        value["statistics"]
    )
    return out


def deserialize_json(data: dict) -> AllowedStatistics:
    out: AllowedStatistics = {}  # type: ignore[typeddict-item]
    if "Statistics" in data:
        import aws_sdk_databrew.types.statistic_list

        out["statistics"] = aws_sdk_databrew.types.statistic_list.deserialize_json(
            data["Statistics"]
        )
    else:
        raise DeserializationError("AllowedStatistics.statistics required")
    return out

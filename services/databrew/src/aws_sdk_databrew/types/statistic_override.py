"""Generated from Smithy shape ``com.amazonaws.databrew#StatisticOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.parameter_map
    import aws_sdk_databrew.types.statistic


class StatisticOverride(TypedDict, closed=True):
    statistic: "aws_sdk_databrew.types.statistic.Statistic"
    """<p>The name of an evaluation</p>"""
    parameters: "aws_sdk_databrew.types.parameter_map.ParameterMap"
    """<p>A map that includes overrides of an evaluation’s parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticOverride) -> dict:
    out: dict = {}
    out["Statistic"] = value["statistic"]
    import aws_sdk_databrew.types.parameter_map

    out["Parameters"] = aws_sdk_databrew.types.parameter_map.serialize_json(
        value["parameters"]
    )
    return out


def deserialize_json(data: dict) -> StatisticOverride:
    out: StatisticOverride = {}  # type: ignore[typeddict-item]
    if "Statistic" in data:
        out["statistic"] = data["Statistic"]
    else:
        raise DeserializationError("StatisticOverride.statistic required")
    if "Parameters" in data:
        import aws_sdk_databrew.types.parameter_map

        out["parameters"] = aws_sdk_databrew.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    else:
        raise DeserializationError("StatisticOverride.parameters required")
    return out

"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RelativeAggregationDuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.time_dimension
    import aws_sdk_lex_models_v2.types.time_value


class RelativeAggregationDuration(TypedDict, closed=True):
    time_dimension: "aws_sdk_lex_models_v2.types.time_dimension.TimeDimension"
    """<p>The type of time period that the <code>timeValue</code> field represents. </p>"""
    time_value: "aws_sdk_lex_models_v2.types.time_value.TimeValue"
    """<p>The period of the time window to gather statistics for. The valid value depends on the setting of the <code>timeDimension</code> field.</p> <ul> <li> <p> <code>Hours</code> - 1/3/6/12/24</p> </li> <li> <p> <code>Days</code> - 3</p> </li> <li> <p> <code>Weeks</code> - 1/2</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelativeAggregationDuration) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.time_dimension

    out["timeDimension"] = aws_sdk_lex_models_v2.types.time_dimension.serialize_json(
        value["time_dimension"]
    )
    out["timeValue"] = value["time_value"]
    return out


def deserialize_json(data: dict) -> RelativeAggregationDuration:
    out: RelativeAggregationDuration = {}  # type: ignore[typeddict-item]
    if "timeDimension" in data:
        import aws_sdk_lex_models_v2.types.time_dimension

        out["time_dimension"] = (
            aws_sdk_lex_models_v2.types.time_dimension.deserialize_json(
                data["timeDimension"]
            )
        )
    else:
        raise DeserializationError(
            "RelativeAggregationDuration.time_dimension required"
        )
    if "timeValue" in data:
        out["time_value"] = data["timeValue"]
    else:
        raise DeserializationError("RelativeAggregationDuration.time_value required")
    return out

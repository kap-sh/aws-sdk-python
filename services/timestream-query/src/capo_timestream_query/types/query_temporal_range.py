"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryTemporalRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.query_temporal_range_max


class QueryTemporalRange(TypedDict, closed=True):
    max: NotRequired[
        "capo_timestream_query.types.query_temporal_range_max.QueryTemporalRangeMax"
    ]
    """<p>Encapsulates the following properties that provide insights into the most sub-optimal performing table on the temporal axis:</p> <ul> <li> <p> <code>Value</code> – The maximum duration in nanoseconds between the start and end of the query.</p> </li> <li> <p> <code>TableArn</code> – The Amazon Resource Name (ARN) of the table which is queried with the largest time range.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryTemporalRange) -> dict:
    out: dict = {}
    if "max" in value:
        import capo_timestream_query.types.query_temporal_range_max

        out["Max"] = (
            capo_timestream_query.types.query_temporal_range_max.serialize_aws_json_1_0(
                value["max"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryTemporalRange:
    out: QueryTemporalRange = {}  # type: ignore[typeddict-item]
    if "Max" in data:
        import capo_timestream_query.types.query_temporal_range_max

        out["max"] = (
            capo_timestream_query.types.query_temporal_range_max.deserialize_aws_json_1_0(
                data["Max"]
            )
        )
    return out

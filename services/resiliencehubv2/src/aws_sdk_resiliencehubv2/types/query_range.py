"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.query_data_point_list
    import aws_sdk_resiliencehubv2.types.query_granularity


class QueryRange(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start time of the query range.</p>"""
    end_time: "datetime.datetime"
    """<p>The end time of the query range.</p>"""
    granularity: "aws_sdk_resiliencehubv2.types.query_granularity.QueryGranularity"
    """<p>The granularity of the query range data points.</p>"""
    data_points: (
        "aws_sdk_resiliencehubv2.types.query_data_point_list.QueryDataPointList"
    )
    """<p>The data points within the query range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryRange) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types._prelude.timestamp

    out["startTime"] = aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_resiliencehubv2.types._prelude.timestamp

    out["endTime"] = aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["end_time"]
    )
    import aws_sdk_resiliencehubv2.types.query_granularity

    out["granularity"] = aws_sdk_resiliencehubv2.types.query_granularity.serialize_json(
        value["granularity"]
    )
    import aws_sdk_resiliencehubv2.types.query_data_point_list

    out["dataPoints"] = (
        aws_sdk_resiliencehubv2.types.query_data_point_list.serialize_json(
            value["data_points"]
        )
    )
    return out


def deserialize_json(data: dict) -> QueryRange:
    out: QueryRange = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("QueryRange.start_time required")
    if "endTime" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    else:
        raise DeserializationError("QueryRange.end_time required")
    if "granularity" in data:
        import aws_sdk_resiliencehubv2.types.query_granularity

        out["granularity"] = (
            aws_sdk_resiliencehubv2.types.query_granularity.deserialize_json(
                data["granularity"]
            )
        )
    else:
        raise DeserializationError("QueryRange.granularity required")
    if "dataPoints" in data:
        import aws_sdk_resiliencehubv2.types.query_data_point_list

        out["data_points"] = (
            aws_sdk_resiliencehubv2.types.query_data_point_list.deserialize_json(
                data["dataPoints"]
            )
        )
    else:
        raise DeserializationError("QueryRange.data_points required")
    return out

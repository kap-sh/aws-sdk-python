"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryDataPoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class QueryDataPoint(TypedDict):
    timestamp: "datetime.datetime"
    """<p>The timestamp of the data point.</p>"""
    query_count: "int"
    """<p>The number of queries at this data point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryDataPoint) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    out["queryCount"] = value["query_count"]
    return out


def deserialize_json(data: dict) -> QueryDataPoint:
    out: QueryDataPoint = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("QueryDataPoint.timestamp required")
    if "queryCount" in data:
        out["query_count"] = data["queryCount"]
    else:
        raise DeserializationError("QueryDataPoint.query_count required")
    return out

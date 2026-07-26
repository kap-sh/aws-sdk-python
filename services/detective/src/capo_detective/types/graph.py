"""Generated from Smithy shape ``com.amazonaws.detective#Graph``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn
    import capo_detective.types.timestamp


class Graph(TypedDict, closed=True):
    arn: NotRequired["capo_detective.types.graph_arn.GraphArn"]
    """<p>The ARN of the behavior graph.</p>"""
    created_time: NotRequired["capo_detective.types.timestamp.Timestamp"]
    """<p>The date and time that the behavior graph was created. The value is an ISO8601 formatted string. For example, <code>2021-08-18T16:35:56.284Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Graph) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_time" in value:
        import capo_detective.types.timestamp

        out["CreatedTime"] = capo_detective.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> Graph:
    out: Graph = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedTime" in data:
        import capo_detective.types.timestamp

        out["created_time"] = capo_detective.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    return out

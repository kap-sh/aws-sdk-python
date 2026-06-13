"""Generated from Smithy shape ``com.amazonaws.rum#QueryFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.query_filter_key
    import aws_sdk_rum.types.query_filter_value_list


class QueryFilter(TypedDict):
    name: NotRequired["aws_sdk_rum.types.query_filter_key.QueryFilterKey"]
    """<p>The name of a key to search for. The filter returns only the events that match the <code>Name</code> and <code>Values</code> that you specify. </p> <p>Valid values for <code>Name</code> are <code>Browser</code> | <code>Device</code> | <code>Country</code> | <code>Page</code> | <code>OS</code> | <code>EventType</code> | <code>Invert</code> </p>"""
    values: NotRequired[
        "aws_sdk_rum.types.query_filter_value_list.QueryFilterValueList"
    ]
    """<p>The values of the <code>Name</code> that are to be be included in the returned results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_rum.types.query_filter_value_list

        out["Values"] = aws_sdk_rum.types.query_filter_value_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> QueryFilter:
    out: QueryFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_rum.types.query_filter_value_list

        out["values"] = aws_sdk_rum.types.query_filter_value_list.deserialize_json(
            data["Values"]
        )
    return out

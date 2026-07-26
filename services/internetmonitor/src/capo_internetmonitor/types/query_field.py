"""Generated from Smithy shape ``com.amazonaws.internetmonitor#QueryField``."""

from typing_extensions import NotRequired, TypedDict


class QueryField(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of a field to query your application's Amazon CloudWatch Internet Monitor data for, such as <code>availability_score</code>.</p>"""
    type: NotRequired["str"]
    """<p>The data type for a query field, which must correspond to the field you're defining for <code>QueryField</code>. For example, if the query field name is <code>availability_score</code>, the data type is <code>float</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryField) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> QueryField:
    out: QueryField = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out

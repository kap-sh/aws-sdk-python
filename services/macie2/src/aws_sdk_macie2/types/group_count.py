"""Generated from Smithy shape ``com.amazonaws.macie2#GroupCount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__string


class GroupCount(TypedDict):
    count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of findings in the group of query results.</p>"""
    group_key: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the property that defines the group in the query results, as specified by the groupBy property in the query request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupCount) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "group_key" in value:
        out["groupKey"] = value["group_key"]
    return out


def deserialize_json(data: dict) -> GroupCount:
    out: GroupCount = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "groupKey" in data:
        out["group_key"] = data["groupKey"]
    return out

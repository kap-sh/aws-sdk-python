"""Generated from Smithy shape ``com.amazonaws.keyspaces#ClusteringKey``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.generic_string
    import aws_sdk_keyspaces.types.sort_order


class ClusteringKey(TypedDict):
    name: "aws_sdk_keyspaces.types.generic_string.GenericString"
    """<p>The name(s) of the clustering column(s).</p>"""
    order_by: "aws_sdk_keyspaces.types.sort_order.SortOrder"
    """<p>Sets the ascendant (<code>ASC</code>) or descendant (<code>DESC</code>) order modifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusteringKey) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["orderBy"] = value["order_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ClusteringKey:
    out: ClusteringKey = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ClusteringKey.name required")
    if "orderBy" in data:
        out["order_by"] = data["orderBy"]
    else:
        raise DeserializationError("ClusteringKey.order_by required")
    return out

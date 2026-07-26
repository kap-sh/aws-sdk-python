"""Generated from Smithy shape ``com.amazonaws.panorama#ListApplicationInstanceNodeInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.next_token
    import capo_panorama.types.node_instances


class ListApplicationInstanceNodeInstancesResponse(TypedDict, closed=True):
    node_instances: NotRequired["capo_panorama.types.node_instances.NodeInstances"]
    """<p>A list of node instances.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationInstanceNodeInstancesResponse) -> dict:
    out: dict = {}
    if "node_instances" in value:
        import capo_panorama.types.node_instances

        out["NodeInstances"] = capo_panorama.types.node_instances.serialize_json(
            value["node_instances"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationInstanceNodeInstancesResponse:
    out: ListApplicationInstanceNodeInstancesResponse = {}  # type: ignore[typeddict-item]
    if "NodeInstances" in data:
        import capo_panorama.types.node_instances

        out["node_instances"] = capo_panorama.types.node_instances.deserialize_json(
            data["NodeInstances"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

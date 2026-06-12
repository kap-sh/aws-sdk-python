"""Generated from Smithy shape ``com.amazonaws.ram#ListResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_list
    import aws_sdk_ram.types.string


class ListResourcesResponse(TypedDict):
    resources: NotRequired["aws_sdk_ram.types.resource_list.ResourceList"]
    """<p>An array of objects that contain information about the resources.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_ram.types.resource_list

        out["resources"] = aws_sdk_ram.types.resource_list.serialize_json(
            value["resources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcesResponse:
    out: ListResourcesResponse = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import aws_sdk_ram.types.resource_list

        out["resources"] = aws_sdk_ram.types.resource_list.deserialize_json(
            data["resources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

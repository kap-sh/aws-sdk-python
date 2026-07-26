"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.resource_arn
    import capo_storage_gateway.types.tags


class ListTagsForResourceOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_storage_gateway.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the resource for which you want to list tags.</p>"""
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to stop returning the list of tags.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>An array that contains the tags for the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Tags" in data:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

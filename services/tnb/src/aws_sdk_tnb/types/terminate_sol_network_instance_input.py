"""Generated from Smithy shape ``com.amazonaws.tnb#TerminateSolNetworkInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.ns_instance_id
    import aws_sdk_tnb.types.tag_map


class TerminateSolNetworkInstanceInput(TypedDict):
    ns_instance_id: "aws_sdk_tnb.types.ns_instance_id.NsInstanceId"
    """<p>ID of the network instance.</p>"""
    tags: NotRequired["aws_sdk_tnb.types.tag_map.TagMap"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateSolNetworkInstanceInput) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TerminateSolNetworkInstanceInput:
    out: TerminateSolNetworkInstanceInput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_tnb.types.tag_map

        out["tags"] = aws_sdk_tnb.types.tag_map.deserialize_json(data["tags"])
    return out

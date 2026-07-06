"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.resource_arn
    import aws_sdk_migrationhuborchestrator.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_migrationhuborchestrator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add tags.</p>"""
    tags: "aws_sdk_migrationhuborchestrator.types.tag_map.TagMap"
    """<p>A collection of labels, in the form of key:value pairs, that apply to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_migrationhuborchestrator.types.tag_map

    out["tags"] = aws_sdk_migrationhuborchestrator.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_migrationhuborchestrator.types.tag_map

        out["tags"] = aws_sdk_migrationhuborchestrator.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

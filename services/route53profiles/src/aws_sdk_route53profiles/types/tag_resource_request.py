"""Generated from Smithy shape ``com.amazonaws.route53profiles#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53profiles.types.arn
    import aws_sdk_route53profiles.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_route53profiles.types.arn.Arn"
    """<p> The Amazon Resource Name (ARN) for the resource that you want to add tags to. </p>"""
    tags: "aws_sdk_route53profiles.types.tag_map.TagMap"
    """<p> The tags that you want to add to the specified resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_route53profiles.types.tag_map

    out["Tags"] = aws_sdk_route53profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_route53profiles.types.tag_map

        out["tags"] = aws_sdk_route53profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.arn
    import aws_sdk_gameliftstreams.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_gameliftstreams.types.arn.Arn"
    """<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> of the Amazon GameLift Streams resource that you want to apply tags to.</p>"""
    tags: "aws_sdk_gameliftstreams.types.tags.Tags"
    """<p>A list of tags, in the form of key-value pairs, to assign to the specified Amazon GameLift Streams resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_gameliftstreams.types.tags

    out["Tags"] = aws_sdk_gameliftstreams.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_gameliftstreams.types.tags

        out["tags"] = aws_sdk_gameliftstreams.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

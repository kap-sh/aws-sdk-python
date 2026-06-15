"""Generated from Smithy shape ``com.amazonaws.oam#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_oam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_oam.types.arn
    import aws_sdk_oam.types.tag_map_input


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_oam.types.arn.Arn"
    r"""<p>The ARN of the resource that you're adding tags to.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\">CloudWatch Logs resources and operations</a>.</p>"""
    tags: "aws_sdk_oam.types.tag_map_input.TagMapInput"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import aws_sdk_oam.types.tag_map_input

    out["Tags"] = aws_sdk_oam.types.tag_map_input.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_oam.types.tag_map_input

        out["tags"] = aws_sdk_oam.types.tag_map_input.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

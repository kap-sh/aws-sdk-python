"""Generated from Smithy shape ``com.amazonaws.synthetics#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.resource_arn
    import aws_sdk_synthetics.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_synthetics.types.resource_arn.ResourceArn"
    """<p>The ARN of the canary or group that you're adding tags to.</p> <p>The ARN format of a canary is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:canary:<i>canary-name</i> </code>.</p> <p>The ARN format of a group is <code>arn:aws:synthetics:<i>Region</i>:<i>account-id</i>:group:<i>group-name</i> </code> </p>"""
    tags: "aws_sdk_synthetics.types.tag_map.TagMap"
    """<p>The list of key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_synthetics.types.tag_map

    out["Tags"] = aws_sdk_synthetics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_synthetics.types.tag_map

        out["tags"] = aws_sdk_synthetics.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsagent#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to tag.</p>"""
    tags: "aws_sdk_devops_agent.types.tags.Tags"
    """<p>Tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.tags

    out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "aws_sdk_devops_agent.types.tags.Tags"
    """<p>Tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.tags

    out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out

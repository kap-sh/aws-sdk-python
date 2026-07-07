"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.create_output_list
    import aws_sdk_elementalinference.types.resource_name
    import aws_sdk_elementalinference.types.tag_map


class CreateFeedRequest(TypedDict, closed=True):
    name: "aws_sdk_elementalinference.types.resource_name.ResourceName"
    """<p>A user-friendly name for this feed.</p>"""
    outputs: "aws_sdk_elementalinference.types.create_output_list.CreateOutputList"
    """<p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>"""
    tags: NotRequired["aws_sdk_elementalinference.types.tag_map.TagMap"]
    """<p>Optional tags. You can also add tags later, using TagResource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFeedRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_elementalinference.types.create_output_list

    out["outputs"] = aws_sdk_elementalinference.types.create_output_list.serialize_json(
        value["outputs"]
    )
    if "tags" in value:
        import aws_sdk_elementalinference.types.tag_map

        out["tags"] = aws_sdk_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFeedRequest:
    out: CreateFeedRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFeedRequest.name required")
    if "outputs" in data:
        import aws_sdk_elementalinference.types.create_output_list

        out["outputs"] = (
            aws_sdk_elementalinference.types.create_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        raise DeserializationError("CreateFeedRequest.outputs required")
    if "tags" in data:
        import aws_sdk_elementalinference.types.tag_map

        out["tags"] = aws_sdk_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out

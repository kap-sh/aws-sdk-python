"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.create_output_list
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map


class CreateFeedRequest(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A user-friendly name for this feed.</p>"""
    outputs: "capo_elementalinference.types.create_output_list.CreateOutputList"
    """<p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>Optional tags. You can also add tags later, using TagResource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFeedRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_elementalinference.types.create_output_list

    out["outputs"] = capo_elementalinference.types.create_output_list.serialize_json(
        value["outputs"]
    )
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
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
        import capo_elementalinference.types.create_output_list

        out["outputs"] = (
            capo_elementalinference.types.create_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        raise DeserializationError("CreateFeedRequest.outputs required")
    if "tags" in data:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out

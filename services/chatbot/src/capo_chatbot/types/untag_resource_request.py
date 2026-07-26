"""Generated from Smithy shape ``com.amazonaws.chatbot#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.amazon_resource_name
    import capo_chatbot.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chatbot.types.amazon_resource_name.AmazonResourceName"
    """<p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.</p>"""
    tag_keys: "capo_chatbot.types.tag_key_list.TagKeyList"
    """<p>TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chatbot.types.tag_key_list

    out["TagKeys"] = capo_chatbot.types.tag_key_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import capo_chatbot.types.tag_key_list

        out["tag_keys"] = capo_chatbot.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

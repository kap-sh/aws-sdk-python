"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn
    import capo_chime_sdk_voice.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_voice.types.arn.Arn"
    """<p>The ARN of the resource being tagged. </p>"""
    tags: "capo_chime_sdk_voice.types.tag_list.TagList"
    """<p>A list of the tags being added to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_voice.types.tag_list

    out["Tags"] = capo_chime_sdk_voice.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

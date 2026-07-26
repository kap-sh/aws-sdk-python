"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The resource ARN.</p>"""
    tags: "capo_chime_sdk_messaging.types.tag_list.TagList"
    """<p>The tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_messaging.types.tag_list

    out["Tags"] = capo_chime_sdk_messaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import capo_chime_sdk_messaging.types.tag_list

        out["tags"] = capo_chime_sdk_messaging.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

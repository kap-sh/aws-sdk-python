"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.arn
    import aws_sdk_chime_sdk_voice.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_chime_sdk_voice.types.arn.Arn"
    """<p>The ARN of the resource having its tags removed.</p>"""
    tag_keys: "aws_sdk_chime_sdk_voice.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags being removed from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_chime_sdk_voice.types.tag_key_list

    out["TagKeys"] = aws_sdk_chime_sdk_voice.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_chime_sdk_voice.types.tag_key_list

        out["tag_keys"] = aws_sdk_chime_sdk_voice.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

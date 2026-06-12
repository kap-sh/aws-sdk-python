"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The resource ARN.</p>"""
    tag_keys: "aws_sdk_chime_sdk_messaging.types.tag_key_list.TagKeyList"
    """<p>The tag keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_chime_sdk_messaging.types.tag_key_list

    out["TagKeys"] = aws_sdk_chime_sdk_messaging.types.tag_key_list.serialize_json(
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
        import aws_sdk_chime_sdk_messaging.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_chime_sdk_messaging.types.tag_key_list.deserialize_json(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

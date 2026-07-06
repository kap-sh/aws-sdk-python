"""Generated from Smithy shape ``com.amazonaws.xray#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.amazon_resource_name
    import aws_sdk_xray.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_xray.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.</p>"""
    tag_keys: "aws_sdk_xray.types.tag_key_list.TagKeyList"
    """<p>Keys for one or more tags that you want to remove from an X-Ray group or sampling rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_xray.types.tag_key_list

    out["TagKeys"] = aws_sdk_xray.types.tag_key_list.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_xray.types.tag_key_list

        out["tag_keys"] = aws_sdk_xray.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

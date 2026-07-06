"""Generated from Smithy shape ``com.amazonaws.waf#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.resource_arn
    import aws_sdk_waf.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_waf.types.resource_arn.ResourceArn"
    """<p></p>"""
    tag_keys: "aws_sdk_waf.types.tag_key_list.TagKeyList"
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_waf.types.tag_key_list

    out["TagKeys"] = aws_sdk_waf.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_waf.types.tag_key_list

        out["tag_keys"] = aws_sdk_waf.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

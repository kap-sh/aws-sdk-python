"""Generated from Smithy shape ``com.amazonaws.interconnect#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.amazon_resource_name
    import aws_sdk_interconnect.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource from which the specified tags should be removed.</p>"""
    tag_keys: "aws_sdk_interconnect.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys that should be removed from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_interconnect.types.tag_key_list

    out["tagKeys"] = aws_sdk_interconnect.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UntagResourceRequest.arn required")
    if "tagKeys" in data:
        import aws_sdk_interconnect.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_interconnect.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

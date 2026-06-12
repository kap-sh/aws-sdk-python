"""Generated from Smithy shape ``com.amazonaws.healthlake#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.amazon_resource_name
    import aws_sdk_healthlake.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_healthlake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the data store from which tags are being removed.</p>"""
    tag_keys: "aws_sdk_healthlake.types.tag_key_list.TagKeyList"
    """<p>The keys for the tags to be removed from the data store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_healthlake.types.tag_key_list

    out["TagKeys"] = aws_sdk_healthlake.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_healthlake.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_healthlake.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

"""Generated from Smithy shape ``com.amazonaws.timestreamquery#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Timestream resource that the tags will be removed from. This value is an Amazon Resource Name (ARN). </p>"""
    tag_keys: "aws_sdk_timestream_query.types.tag_key_list.TagKeyList"
    """<p>A list of tags keys. Existing tags of the resource whose keys are members of this list will be removed from the Timestream resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_timestream_query.types.tag_key_list

    out["TagKeys"] = aws_sdk_timestream_query.types.tag_key_list.serialize_aws_json_1_0(
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
        import aws_sdk_timestream_query.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_timestream_query.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

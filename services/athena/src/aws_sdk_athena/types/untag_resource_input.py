"""Generated from Smithy shape ``com.amazonaws.athena#UntagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.amazon_resource_name
    import aws_sdk_athena.types.tag_key_list


class UntagResourceInput(TypedDict):
    resource_arn: "aws_sdk_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>Specifies the ARN of the resource from which tags are to be removed.</p>"""
    tag_keys: "aws_sdk_athena.types.tag_key_list.TagKeyList"
    """<p>A comma-separated list of one or more tag keys whose tags are to be removed from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_athena.types.tag_key_list

    out["TagKeys"] = aws_sdk_athena.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "TagKeys" in data:
        import aws_sdk_athena.types.tag_key_list

        out["tag_keys"] = aws_sdk_athena.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out

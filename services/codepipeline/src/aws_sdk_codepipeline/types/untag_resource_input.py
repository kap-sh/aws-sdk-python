"""Generated from Smithy shape ``com.amazonaws.codepipeline#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.resource_arn
    import aws_sdk_codepipeline.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_codepipeline.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "aws_sdk_codepipeline.types.tag_key_list.TagKeyList"
    """<p>The list of keys for the tags to be removed from the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_codepipeline.types.tag_key_list

    out["tagKeys"] = aws_sdk_codepipeline.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_codepipeline.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_codepipeline.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out

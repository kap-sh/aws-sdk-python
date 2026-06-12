"""Generated from Smithy shape ``com.amazonaws.codepipeline#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.resource_arn
    import aws_sdk_codepipeline.types.tag_list


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_codepipeline.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource you want to add tags to.</p>"""
    tags: "aws_sdk_codepipeline.types.tag_list.TagList"
    """<p>The tags you want to modify or add to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_codepipeline.types.tag_list

    out["tags"] = aws_sdk_codepipeline.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "tags" in data:
        import aws_sdk_codepipeline.types.tag_list

        out["tags"] = aws_sdk_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

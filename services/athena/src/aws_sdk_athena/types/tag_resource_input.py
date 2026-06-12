"""Generated from Smithy shape ``com.amazonaws.athena#TagResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.amazon_resource_name
    import aws_sdk_athena.types.tag_list


class TagResourceInput(TypedDict):
    resource_arn: "aws_sdk_athena.types.amazon_resource_name.AmazonResourceName"
    """<p>Specifies the ARN of the Athena resource to which tags are to be added.</p>"""
    tags: "aws_sdk_athena.types.tag_list.TagList"
    """<p>A collection of one or more tags, separated by commas, to be added to an Athena resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_athena.types.tag_list

    out["Tags"] = aws_sdk_athena.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_athena.types.tag_list

        out["tags"] = aws_sdk_athena.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

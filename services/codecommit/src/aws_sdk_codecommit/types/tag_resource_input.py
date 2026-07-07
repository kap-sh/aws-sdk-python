"""Generated from Smithy shape ``com.amazonaws.codecommit#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.resource_arn
    import aws_sdk_codecommit.types.tags_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_codecommit.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.</p>"""
    tags: "aws_sdk_codecommit.types.tags_map.TagsMap"
    """<p>The key-value pair to use when tagging this repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_codecommit.types.tags_map

    out["tags"] = aws_sdk_codecommit.types.tags_map.serialize_aws_json_1_1(
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
        import aws_sdk_codecommit.types.tags_map

        out["tags"] = aws_sdk_codecommit.types.tags_map.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

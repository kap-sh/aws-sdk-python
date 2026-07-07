"""Generated from Smithy shape ``com.amazonaws.codestarconnections#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.amazon_resource_name
    import aws_sdk_codestar_connections.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_codestar_connections.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.</p>"""
    tags: "aws_sdk_codestar_connections.types.tag_list.TagList"
    """<p>The tags you want to modify or add to the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_codestar_connections.types.tag_list

    out["Tags"] = aws_sdk_codestar_connections.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if "Tags" in data:
        import aws_sdk_codestar_connections.types.tag_list

        out["tags"] = (
            aws_sdk_codestar_connections.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out

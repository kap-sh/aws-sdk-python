"""Generated from Smithy shape ``com.amazonaws.keyspaces#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn
    import aws_sdk_keyspaces.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon Keyspaces resource to which to add tags.</p>"""
    tags: "aws_sdk_keyspaces.types.tag_list.TagList"
    """<p>The tags to be assigned to the Amazon Keyspaces resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_keyspaces.types.tag_list

    out["tags"] = aws_sdk_keyspaces.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_keyspaces.types.tag_list

        out["tags"] = aws_sdk_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

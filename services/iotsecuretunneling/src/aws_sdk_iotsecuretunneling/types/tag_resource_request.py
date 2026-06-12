"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsecuretunneling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.amazon_resource_name
    import aws_sdk_iotsecuretunneling.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource.</p>"""
    tags: "aws_sdk_iotsecuretunneling.types.tag_list.TagList"
    """<p>The tags for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_iotsecuretunneling.types.tag_list

    out["tags"] = aws_sdk_iotsecuretunneling.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_iotsecuretunneling.types.tag_list

        out["tags"] = (
            aws_sdk_iotsecuretunneling.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.odb#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_arn


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_odb.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to apply tags to.</p>"""
    tags: "aws_sdk_odb.types.request_tag_map.RequestTagMap"
    """<p>The list of tags to apply to the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_odb.types.request_tag_map

    out["tags"] = aws_sdk_odb.types.request_tag_map.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "tags" in data:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

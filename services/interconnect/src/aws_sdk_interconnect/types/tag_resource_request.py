"""Generated from Smithy shape ``com.amazonaws.interconnect#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.amazon_resource_name
    import aws_sdk_interconnect.types.tag_map


class TagResourceRequest(TypedDict):
    arn: "aws_sdk_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource that should receive the new tags.</p>"""
    tags: "aws_sdk_interconnect.types.tag_map.TagMap"
    """<p>A map of tags to apply to the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_interconnect.types.tag_map

    out["tags"] = aws_sdk_interconnect.types.tag_map.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("TagResourceRequest.arn required")
    if "tags" in data:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

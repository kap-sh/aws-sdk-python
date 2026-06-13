"""Generated from Smithy shape ``com.amazonaws.pcs#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.arn
    import aws_sdk_pcs.types.request_tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_pcs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "aws_sdk_pcs.types.request_tag_map.RequestTagMap"
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_pcs.types.request_tag_map

    out["tags"] = aws_sdk_pcs.types.request_tag_map.serialize_aws_json_1_0(
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
        import aws_sdk_pcs.types.request_tag_map

        out["tags"] = aws_sdk_pcs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

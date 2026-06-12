"""Generated from Smithy shape ``com.amazonaws.emrserverless#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.resource_arn
    import aws_sdk_emr_serverless.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_emr_serverless.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>"""
    tags: "aws_sdk_emr_serverless.types.tag_map.TagMap"
    """<p>The tags to add to the resource. A tag is an array of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_emr_serverless.types.tag_map

    out["tags"] = aws_sdk_emr_serverless.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_emr_serverless.types.tag_map

        out["tags"] = aws_sdk_emr_serverless.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

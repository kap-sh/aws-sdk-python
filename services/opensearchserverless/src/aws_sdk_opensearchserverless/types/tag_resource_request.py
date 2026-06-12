"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.arn
    import aws_sdk_opensearchserverless.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_opensearchserverless.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>"""
    tags: "aws_sdk_opensearchserverless.types.tags.Tags"
    """<p>A list of tags (key-value pairs) to add to the resource. All tag keys in the request must be unique.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_opensearchserverless.types.tags

    out["tags"] = aws_sdk_opensearchserverless.types.tags.serialize_aws_json_1_0(
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
        import aws_sdk_opensearchserverless.types.tags

        out["tags"] = aws_sdk_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

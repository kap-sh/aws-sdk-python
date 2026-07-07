"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.arn
    import aws_sdk_opensearchserverless.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_opensearchserverless.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>"""
    tag_keys: "aws_sdk_opensearchserverless.types.tag_keys.TagKeys"
    """<p>The tag or set of tags to remove from the resource. All tag keys in the request must be unique.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_opensearchserverless.types.tag_keys

    out["tagKeys"] = aws_sdk_opensearchserverless.types.tag_keys.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_opensearchserverless.types.tag_keys

        out["tag_keys"] = (
            aws_sdk_opensearchserverless.types.tag_keys.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

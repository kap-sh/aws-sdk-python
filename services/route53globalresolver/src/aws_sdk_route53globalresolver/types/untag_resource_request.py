"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "aws_sdk_route53globalresolver.types.tag_keys.TagKeys"
    """<p>The tag keys associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_route53globalresolver.types.tag_keys

    out["tagKeys"] = aws_sdk_route53globalresolver.types.tag_keys.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if "tagKeys" in data:
        import aws_sdk_route53globalresolver.types.tag_keys

        out["tag_keys"] = aws_sdk_route53globalresolver.types.tag_keys.deserialize_json(
            data["tagKeys"]
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out

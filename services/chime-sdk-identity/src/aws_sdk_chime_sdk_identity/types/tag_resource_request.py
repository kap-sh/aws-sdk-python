"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The resource ARN.</p>"""
    tags: "aws_sdk_chime_sdk_identity.types.tag_list.TagList"
    """<p>The tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_chime_sdk_identity.types.tag_list

    out["Tags"] = aws_sdk_chime_sdk_identity.types.tag_list.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_chime_sdk_identity.types.tag_list

        out["tags"] = aws_sdk_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notificationscontacts.types.email_contact_arn
    import aws_sdk_notificationscontacts.types.tag_map


class TagResourceRequest(TypedDict):
    arn: "aws_sdk_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The ARN of the configuration.</p>"""
    tags: "aws_sdk_notificationscontacts.types.tag_map.TagMap"
    """<p>A list of tags to apply to the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_notificationscontacts.types.tag_map

    out["tags"] = aws_sdk_notificationscontacts.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_notificationscontacts.types.tag_map

        out["tags"] = aws_sdk_notificationscontacts.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

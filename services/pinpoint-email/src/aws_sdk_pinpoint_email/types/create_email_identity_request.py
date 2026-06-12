"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateEmailIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.identity
    import aws_sdk_pinpoint_email.types.tag_list


class CreateEmailIdentityRequest(TypedDict):
    email_identity: "aws_sdk_pinpoint_email.types.identity.Identity"
    """<p>The email address or domain that you want to verify.</p>"""
    tags: NotRequired["aws_sdk_pinpoint_email.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that you want to associate with the email identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "tags" in value:
        import aws_sdk_pinpoint_email.types.tag_list

        out["Tags"] = aws_sdk_pinpoint_email.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityRequest:
    out: CreateEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    if "EmailIdentity" in data:
        out["email_identity"] = data["EmailIdentity"]
    else:
        raise DeserializationError("CreateEmailIdentityRequest.email_identity required")
    if "Tags" in data:
        import aws_sdk_pinpoint_email.types.tag_list

        out["tags"] = aws_sdk_pinpoint_email.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out

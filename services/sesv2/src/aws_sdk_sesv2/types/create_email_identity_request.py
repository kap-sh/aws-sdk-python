"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateEmailIdentityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.dkim_signing_attributes
    import aws_sdk_sesv2.types.identity
    import aws_sdk_sesv2.types.tag_list


class CreateEmailIdentityRequest(TypedDict):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The email address or domain to verify.</p>"""
    tags: NotRequired["aws_sdk_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) to associate with the email identity.</p>"""
    dkim_signing_attributes: NotRequired[
        "aws_sdk_sesv2.types.dkim_signing_attributes.DkimSigningAttributes"
    ]
    """<p>If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\">Easy DKIM</a>.</p> <p>You can only specify this object if the email identity is a domain, as opposed to an address.</p>"""
    configuration_set_name: NotRequired[
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The configuration set to use by default when sending from this identity. Note that any configuration set defined in the email sending request takes precedence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "tags" in value:
        import aws_sdk_sesv2.types.tag_list

        out["Tags"] = aws_sdk_sesv2.types.tag_list.serialize_json(value["tags"])
    if "dkim_signing_attributes" in value:
        import aws_sdk_sesv2.types.dkim_signing_attributes

        out["DkimSigningAttributes"] = (
            aws_sdk_sesv2.types.dkim_signing_attributes.serialize_json(
                value["dkim_signing_attributes"]
            )
        )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityRequest:
    out: CreateEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    if "EmailIdentity" in data:
        out["email_identity"] = data["EmailIdentity"]
    else:
        raise DeserializationError("CreateEmailIdentityRequest.email_identity required")
    if "Tags" in data:
        import aws_sdk_sesv2.types.tag_list

        out["tags"] = aws_sdk_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "DkimSigningAttributes" in data:
        import aws_sdk_sesv2.types.dkim_signing_attributes

        out["dkim_signing_attributes"] = (
            aws_sdk_sesv2.types.dkim_signing_attributes.deserialize_json(
                data["DkimSigningAttributes"]
            )
        )
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out

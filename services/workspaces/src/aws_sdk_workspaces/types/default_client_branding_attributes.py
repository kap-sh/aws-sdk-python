"""Generated from Smithy shape ``com.amazonaws.workspaces#DefaultClientBrandingAttributes``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.client_email
    import aws_sdk_workspaces.types.client_url
    import aws_sdk_workspaces.types.login_message


class DefaultClientBrandingAttributes(TypedDict):
    logo_url: NotRequired["aws_sdk_workspaces.types.client_url.ClientUrl"]
    """<p>The logo. The only image format accepted is a binary data object that is converted from a <code>.png</code> file.</p>"""
    support_email: NotRequired["aws_sdk_workspaces.types.client_email.ClientEmail"]
    """<p>The support email. The company's customer support email address.</p> <note> <ul> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive. You can specify one parameter for each platform type, but not both.</p> </li> <li> <p>The default email is <code>workspaces-feedback@amazon.com</code>.</p> </li> </ul> </note>"""
    support_link: NotRequired["aws_sdk_workspaces.types.client_url.ClientUrl"]
    """<p>The support link. The link for the company's customer support page for their WorkSpace.</p> <note> <ul> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive.You can specify one parameter for each platform type, but not both.</p> </li> <li> <p>The default support link is <code>workspaces-feedback@amazon.com</code>.</p> </li> </ul> </note>"""
    forgot_password_link: NotRequired["aws_sdk_workspaces.types.client_url.ClientUrl"]
    """<p>The forgotten password link. This is the web address that users can go to if they forget the password for their WorkSpace.</p>"""
    login_message: NotRequired["aws_sdk_workspaces.types.login_message.LoginMessage"]
    """<p>The login message. Specified as a key value pair, in which the key is a locale and the value is the localized message for that locale. The only key supported is <code>en_US</code>. The HTML tags supported include the following: <code>a, b, blockquote, br, cite, code, dd, dl, dt, div, em, i, li, ol, p, pre, q, small, span, strike, strong, sub, sup, u, ul</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultClientBrandingAttributes) -> dict:
    out: dict = {}
    if "logo_url" in value:
        out["LogoUrl"] = value["logo_url"]
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_link" in value:
        out["SupportLink"] = value["support_link"]
    if "forgot_password_link" in value:
        out["ForgotPasswordLink"] = value["forgot_password_link"]
    if "login_message" in value:
        import aws_sdk_workspaces.types.login_message

        out["LoginMessage"] = (
            aws_sdk_workspaces.types.login_message.serialize_aws_json_1_1(
                value["login_message"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultClientBrandingAttributes:
    out: DefaultClientBrandingAttributes = {}  # type: ignore[typeddict-item]
    if "LogoUrl" in data:
        out["logo_url"] = data["LogoUrl"]
    if "SupportEmail" in data:
        out["support_email"] = data["SupportEmail"]
    if "SupportLink" in data:
        out["support_link"] = data["SupportLink"]
    if "ForgotPasswordLink" in data:
        out["forgot_password_link"] = data["ForgotPasswordLink"]
    if "LoginMessage" in data:
        import aws_sdk_workspaces.types.login_message

        out["login_message"] = (
            aws_sdk_workspaces.types.login_message.deserialize_aws_json_1_1(
                data["LoginMessage"]
            )
        )
    return out

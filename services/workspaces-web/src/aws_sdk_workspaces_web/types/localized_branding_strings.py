"""Generated from Smithy shape ``com.amazonaws.workspacesweb#LocalizedBrandingStrings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.branding_safe_string_type
    import aws_sdk_workspaces_web.types.contact_link_url


class LocalizedBrandingStrings(TypedDict, closed=True):
    browser_tab_title: (
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    )
    """<p>The text displayed in the browser tab title.</p>"""
    welcome_text: (
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    )
    """<p>The welcome text displayed on the sign-in page.</p>"""
    login_title: NotRequired[
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    r"""<p>The title text for the login section. This field is optional and defaults to \"Sign In\".</p>"""
    login_description: NotRequired[
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    r"""<p>The description text for the login section. This field is optional and defaults to \"Sign in to your session\".</p>"""
    login_button_text: NotRequired[
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    r"""<p>The text displayed on the login button. This field is optional and defaults to \"Sign In\".</p>"""
    contact_link: NotRequired[
        "aws_sdk_workspaces_web.types.contact_link_url.ContactLinkUrl"
    ]
    """<p>A contact link URL. The URL must start with <code>https://</code> or <code>mailto:</code>. If not provided, the contact button will be hidden from the web portal screen.</p>"""
    contact_button_text: NotRequired[
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    r"""<p>The text displayed on the contact button. This field is optional and defaults to \"Contact us\".</p>"""
    loading_text: NotRequired[
        "aws_sdk_workspaces_web.types.branding_safe_string_type.BrandingSafeStringType"
    ]
    r"""<p>The text displayed during session loading. This field is optional and defaults to \"Loading your session\".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalizedBrandingStrings) -> dict:
    out: dict = {}
    out["browserTabTitle"] = value["browser_tab_title"]
    out["welcomeText"] = value["welcome_text"]
    if "login_title" in value:
        out["loginTitle"] = value["login_title"]
    if "login_description" in value:
        out["loginDescription"] = value["login_description"]
    if "login_button_text" in value:
        out["loginButtonText"] = value["login_button_text"]
    if "contact_link" in value:
        out["contactLink"] = value["contact_link"]
    if "contact_button_text" in value:
        out["contactButtonText"] = value["contact_button_text"]
    if "loading_text" in value:
        out["loadingText"] = value["loading_text"]
    return out


def deserialize_json(data: dict) -> LocalizedBrandingStrings:
    out: LocalizedBrandingStrings = {}  # type: ignore[typeddict-item]
    if "browserTabTitle" in data:
        out["browser_tab_title"] = data["browserTabTitle"]
    else:
        raise DeserializationError(
            "LocalizedBrandingStrings.browser_tab_title required"
        )
    if "welcomeText" in data:
        out["welcome_text"] = data["welcomeText"]
    else:
        raise DeserializationError("LocalizedBrandingStrings.welcome_text required")
    if "loginTitle" in data:
        out["login_title"] = data["loginTitle"]
    if "loginDescription" in data:
        out["login_description"] = data["loginDescription"]
    if "loginButtonText" in data:
        out["login_button_text"] = data["loginButtonText"]
    if "contactLink" in data:
        out["contact_link"] = data["contactLink"]
    if "contactButtonText" in data:
        out["contact_button_text"] = data["contactButtonText"]
    if "loadingText" in data:
        out["loading_text"] = data["loadingText"]
    return out

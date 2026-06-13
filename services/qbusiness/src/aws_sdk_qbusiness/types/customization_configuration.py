"""Generated from Smithy shape ``com.amazonaws.qbusiness#CustomizationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.custom_css_url
    import aws_sdk_qbusiness.types.favicon_url
    import aws_sdk_qbusiness.types.font_url
    import aws_sdk_qbusiness.types.logo_url


class CustomizationConfiguration(TypedDict):
    custom_css_url: NotRequired["aws_sdk_qbusiness.types.custom_css_url.CustomCSSUrl"]
    """<p>Provides the URL where the custom CSS file is hosted for an Amazon Q web experience.</p>"""
    logo_url: NotRequired["aws_sdk_qbusiness.types.logo_url.LogoUrl"]
    """<p>Provides the URL where the custom logo file is hosted for an Amazon Q web experience.</p>"""
    font_url: NotRequired["aws_sdk_qbusiness.types.font_url.FontUrl"]
    """<p>Provides the URL where the custom font file is hosted for an Amazon Q web experience.</p>"""
    favicon_url: NotRequired["aws_sdk_qbusiness.types.favicon_url.FaviconUrl"]
    """<p>Provides the URL where the custom favicon file is hosted for an Amazon Q web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomizationConfiguration) -> dict:
    out: dict = {}
    if "custom_css_url" in value:
        out["customCSSUrl"] = value["custom_css_url"]
    if "logo_url" in value:
        out["logoUrl"] = value["logo_url"]
    if "font_url" in value:
        out["fontUrl"] = value["font_url"]
    if "favicon_url" in value:
        out["faviconUrl"] = value["favicon_url"]
    return out


def deserialize_json(data: dict) -> CustomizationConfiguration:
    out: CustomizationConfiguration = {}  # type: ignore[typeddict-item]
    if "customCSSUrl" in data:
        out["custom_css_url"] = data["customCSSUrl"]
    if "logoUrl" in data:
        out["logo_url"] = data["logoUrl"]
    if "fontUrl" in data:
        out["font_url"] = data["fontUrl"]
    if "faviconUrl" in data:
        out["favicon_url"] = data["faviconUrl"]
    return out

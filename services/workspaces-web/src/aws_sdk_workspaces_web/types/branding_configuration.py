"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrandingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces_web.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.color_theme
    import aws_sdk_workspaces_web.types.image_metadata
    import aws_sdk_workspaces_web.types.localized_branding_string_map
    import aws_sdk_workspaces_web.types.markdown

class BrandingConfiguration(TypedDict):
    logo: "aws_sdk_workspaces_web.types.image_metadata.ImageMetadata"
    """<p>Metadata for the logo image file, including the MIME type, file extension, and upload timestamp.</p>"""
    wallpaper: NotRequired["aws_sdk_workspaces_web.types.image_metadata.ImageMetadata"]
    """<p>Metadata for the wallpaper image file, including the MIME type, file extension, and upload timestamp.</p>"""
    favicon: "aws_sdk_workspaces_web.types.image_metadata.ImageMetadata"
    """<p>Metadata for the favicon image file, including the MIME type, file extension, and upload timestamp.</p>"""
    localized_strings: "aws_sdk_workspaces_web.types.localized_branding_string_map.LocalizedBrandingStringMap"
    """<p>A map of localized text strings for different languages, allowing the portal to display content in the user's preferred language.</p>"""
    color_theme: "aws_sdk_workspaces_web.types.color_theme.ColorTheme"
    """<p>The color theme for components on the web portal.</p>"""
    terms_of_service: NotRequired["aws_sdk_workspaces_web.types.markdown.Markdown"]
    """<p>The terms of service text in Markdown format that users must accept before accessing the portal.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BrandingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.image_metadata
    out["logo"] = aws_sdk_workspaces_web.types.image_metadata.serialize_json(value["logo"])
    if "wallpaper" in value:
        import aws_sdk_workspaces_web.types.image_metadata
        out["wallpaper"] = aws_sdk_workspaces_web.types.image_metadata.serialize_json(value["wallpaper"])
    import aws_sdk_workspaces_web.types.image_metadata
    out["favicon"] = aws_sdk_workspaces_web.types.image_metadata.serialize_json(value["favicon"])
    import aws_sdk_workspaces_web.types.localized_branding_string_map
    out["localizedStrings"] = aws_sdk_workspaces_web.types.localized_branding_string_map.serialize_json(value["localized_strings"])
    import aws_sdk_workspaces_web.types.color_theme
    out["colorTheme"] = aws_sdk_workspaces_web.types.color_theme.serialize_json(value["color_theme"])
    if "terms_of_service" in value:
        out["termsOfService"] = value["terms_of_service"]
    return out


def deserialize_json(data: dict) -> BrandingConfiguration:
    out: BrandingConfiguration = {}  # type: ignore[typeddict-item]
    if "logo" in data:
        import aws_sdk_workspaces_web.types.image_metadata
        out["logo"] = aws_sdk_workspaces_web.types.image_metadata.deserialize_json(data["logo"])
    else:
        raise DeserializationError("BrandingConfiguration.logo required")
    if "wallpaper" in data:
        import aws_sdk_workspaces_web.types.image_metadata
        out["wallpaper"] = aws_sdk_workspaces_web.types.image_metadata.deserialize_json(data["wallpaper"])
    if "favicon" in data:
        import aws_sdk_workspaces_web.types.image_metadata
        out["favicon"] = aws_sdk_workspaces_web.types.image_metadata.deserialize_json(data["favicon"])
    else:
        raise DeserializationError("BrandingConfiguration.favicon required")
    if "localizedStrings" in data:
        import aws_sdk_workspaces_web.types.localized_branding_string_map
        out["localized_strings"] = aws_sdk_workspaces_web.types.localized_branding_string_map.deserialize_json(data["localizedStrings"])
    else:
        raise DeserializationError("BrandingConfiguration.localized_strings required")
    if "colorTheme" in data:
        import aws_sdk_workspaces_web.types.color_theme
        out["color_theme"] = aws_sdk_workspaces_web.types.color_theme.deserialize_json(data["colorTheme"])
    else:
        raise DeserializationError("BrandingConfiguration.color_theme required")
    if "termsOfService" in data:
        out["terms_of_service"] = data["termsOfService"]
    return out
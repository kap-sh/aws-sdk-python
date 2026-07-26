"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeFooterLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.theme_footer_link_display_name
    import capo_appstream.types.theme_footer_link_url


class ThemeFooterLink(TypedDict, closed=True):
    display_name: NotRequired[
        "capo_appstream.types.theme_footer_link_display_name.ThemeFooterLinkDisplayName"
    ]
    """<p>The name of the websites that display in the catalog page footer.</p>"""
    footer_link_url: NotRequired[
        "capo_appstream.types.theme_footer_link_url.ThemeFooterLinkURL"
    ]
    """<p>The URL of the websites that display in the catalog page footer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeFooterLink) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "footer_link_url" in value:
        out["FooterLinkURL"] = value["footer_link_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThemeFooterLink:
    out: ThemeFooterLink = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "FooterLinkURL" in data:
        out["footer_link_url"] = data["FooterLinkURL"]
    return out

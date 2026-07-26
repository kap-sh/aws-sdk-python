"""Generated from Smithy shape ``com.amazonaws.appstream#Theme``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name
    import capo_appstream.types.string
    import capo_appstream.types.theme_footer_links
    import capo_appstream.types.theme_state
    import capo_appstream.types.theme_styling
    import capo_appstream.types.theme_title_text
    import capo_appstream.types.timestamp


class Theme(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The stack that has the custom branding theme.</p>"""
    state: NotRequired["capo_appstream.types.theme_state.ThemeState"]
    """<p>The state of the theme.</p>"""
    theme_title_text: NotRequired[
        "capo_appstream.types.theme_title_text.ThemeTitleText"
    ]
    """<p>The browser tab page title.</p>"""
    theme_styling: NotRequired["capo_appstream.types.theme_styling.ThemeStyling"]
    """<p>The color that is used for the website links, text, buttons, and catalog page background.</p>"""
    theme_footer_links: NotRequired[
        "capo_appstream.types.theme_footer_links.ThemeFooterLinks"
    ]
    """<p>The website links that display in the catalog page footer.</p>"""
    theme_organization_logo_url: NotRequired["capo_appstream.types.string.String"]
    """<p>The URL of the logo that displays in the catalog page header.</p>"""
    theme_favicon_url: NotRequired["capo_appstream.types.string.String"]
    """<p>The URL of the icon that displays at the top of a user's browser tab during streaming sessions.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time the theme was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Theme) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "state" in value:
        import capo_appstream.types.theme_state

        out["State"] = capo_appstream.types.theme_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "theme_title_text" in value:
        out["ThemeTitleText"] = value["theme_title_text"]
    if "theme_styling" in value:
        import capo_appstream.types.theme_styling

        out["ThemeStyling"] = capo_appstream.types.theme_styling.serialize_aws_json_1_1(
            value["theme_styling"]
        )
    if "theme_footer_links" in value:
        import capo_appstream.types.theme_footer_links

        out["ThemeFooterLinks"] = (
            capo_appstream.types.theme_footer_links.serialize_aws_json_1_1(
                value["theme_footer_links"]
            )
        )
    if "theme_organization_logo_url" in value:
        out["ThemeOrganizationLogoURL"] = value["theme_organization_logo_url"]
    if "theme_favicon_url" in value:
        out["ThemeFaviconURL"] = value["theme_favicon_url"]
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Theme:
    out: Theme = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "State" in data:
        import capo_appstream.types.theme_state

        out["state"] = capo_appstream.types.theme_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "ThemeTitleText" in data:
        out["theme_title_text"] = data["ThemeTitleText"]
    if "ThemeStyling" in data:
        import capo_appstream.types.theme_styling

        out["theme_styling"] = (
            capo_appstream.types.theme_styling.deserialize_aws_json_1_1(
                data["ThemeStyling"]
            )
        )
    if "ThemeFooterLinks" in data:
        import capo_appstream.types.theme_footer_links

        out["theme_footer_links"] = (
            capo_appstream.types.theme_footer_links.deserialize_aws_json_1_1(
                data["ThemeFooterLinks"]
            )
        )
    if "ThemeOrganizationLogoURL" in data:
        out["theme_organization_logo_url"] = data["ThemeOrganizationLogoURL"]
    if "ThemeFaviconURL" in data:
        out["theme_favicon_url"] = data["ThemeFaviconURL"]
    if "CreatedTime" in data:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    return out

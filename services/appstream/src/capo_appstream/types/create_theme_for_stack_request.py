"""Generated from Smithy shape ``com.amazonaws.appstream#CreateThemeForStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name
    import capo_appstream.types.s3_location
    import capo_appstream.types.theme_footer_links
    import capo_appstream.types.theme_styling
    import capo_appstream.types.theme_title_text


class CreateThemeForStackRequest(TypedDict, closed=True):
    stack_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the stack for the theme.</p>"""
    footer_links: NotRequired[
        "capo_appstream.types.theme_footer_links.ThemeFooterLinks"
    ]
    """<p>The links that are displayed in the footer of the streaming application catalog page. These links are helpful resources for users, such as the organization's IT support and product marketing sites.</p>"""
    title_text: NotRequired["capo_appstream.types.theme_title_text.ThemeTitleText"]
    """<p>The title that is displayed at the top of the browser tab during users' application streaming sessions.</p>"""
    theme_styling: NotRequired["capo_appstream.types.theme_styling.ThemeStyling"]
    """<p>The color theme that is applied to website links, text, and buttons. These colors are also applied as accents in the background for the streaming application catalog page.</p>"""
    organization_logo_s3_location: NotRequired[
        "capo_appstream.types.s3_location.S3Location"
    ]
    """<p>The organization logo that appears on the streaming application catalog page.</p>"""
    favicon_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The S3 location of the favicon. The favicon enables users to recognize their application streaming site in a browser full of tabs or bookmarks. It is displayed at the top of the browser tab for the application streaming site during users' streaming sessions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateThemeForStackRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "footer_links" in value:
        import capo_appstream.types.theme_footer_links

        out["FooterLinks"] = (
            capo_appstream.types.theme_footer_links.serialize_aws_json_1_1(
                value["footer_links"]
            )
        )
    if "title_text" in value:
        out["TitleText"] = value["title_text"]
    if "theme_styling" in value:
        import capo_appstream.types.theme_styling

        out["ThemeStyling"] = capo_appstream.types.theme_styling.serialize_aws_json_1_1(
            value["theme_styling"]
        )
    if "organization_logo_s3_location" in value:
        import capo_appstream.types.s3_location

        out["OrganizationLogoS3Location"] = (
            capo_appstream.types.s3_location.serialize_aws_json_1_1(
                value["organization_logo_s3_location"]
            )
        )
    if "favicon_s3_location" in value:
        import capo_appstream.types.s3_location

        out["FaviconS3Location"] = (
            capo_appstream.types.s3_location.serialize_aws_json_1_1(
                value["favicon_s3_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateThemeForStackRequest:
    out: CreateThemeForStackRequest = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "FooterLinks" in data:
        import capo_appstream.types.theme_footer_links

        out["footer_links"] = (
            capo_appstream.types.theme_footer_links.deserialize_aws_json_1_1(
                data["FooterLinks"]
            )
        )
    if "TitleText" in data:
        out["title_text"] = data["TitleText"]
    if "ThemeStyling" in data:
        import capo_appstream.types.theme_styling

        out["theme_styling"] = (
            capo_appstream.types.theme_styling.deserialize_aws_json_1_1(
                data["ThemeStyling"]
            )
        )
    if "OrganizationLogoS3Location" in data:
        import capo_appstream.types.s3_location

        out["organization_logo_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["OrganizationLogoS3Location"]
            )
        )
    if "FaviconS3Location" in data:
        import capo_appstream.types.s3_location

        out["favicon_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["FaviconS3Location"]
            )
        )
    return out

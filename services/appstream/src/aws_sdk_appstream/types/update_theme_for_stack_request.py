"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateThemeForStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.s3_location
    import aws_sdk_appstream.types.theme_attributes
    import aws_sdk_appstream.types.theme_footer_links
    import aws_sdk_appstream.types.theme_state
    import aws_sdk_appstream.types.theme_styling
    import aws_sdk_appstream.types.theme_title_text


class UpdateThemeForStackRequest(TypedDict, closed=True):
    stack_name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the stack for the theme.</p>"""
    footer_links: NotRequired[
        "aws_sdk_appstream.types.theme_footer_links.ThemeFooterLinks"
    ]
    """<p>The links that are displayed in the footer of the streaming application catalog page. These links are helpful resources for users, such as the organization's IT support and product marketing sites.</p>"""
    title_text: NotRequired["aws_sdk_appstream.types.theme_title_text.ThemeTitleText"]
    """<p>The title that is displayed at the top of the browser tab during users' application streaming sessions.</p>"""
    theme_styling: NotRequired["aws_sdk_appstream.types.theme_styling.ThemeStyling"]
    """<p>The color theme that is applied to website links, text, and buttons. These colors are also applied as accents in the background for the streaming application catalog page.</p>"""
    organization_logo_s3_location: NotRequired[
        "aws_sdk_appstream.types.s3_location.S3Location"
    ]
    """<p>The organization logo that appears on the streaming application catalog page.</p>"""
    favicon_s3_location: NotRequired["aws_sdk_appstream.types.s3_location.S3Location"]
    """<p>The S3 location of the favicon. The favicon enables users to recognize their application streaming site in a browser full of tabs or bookmarks. It is displayed at the top of the browser tab for the application streaming site during users' streaming sessions.</p>"""
    state: NotRequired["aws_sdk_appstream.types.theme_state.ThemeState"]
    """<p>Specifies whether custom branding should be applied to catalog page or not.</p>"""
    attributes_to_delete: NotRequired[
        "aws_sdk_appstream.types.theme_attributes.ThemeAttributes"
    ]
    """<p>The attributes to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateThemeForStackRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "footer_links" in value:
        import aws_sdk_appstream.types.theme_footer_links

        out["FooterLinks"] = (
            aws_sdk_appstream.types.theme_footer_links.serialize_aws_json_1_1(
                value["footer_links"]
            )
        )
    if "title_text" in value:
        out["TitleText"] = value["title_text"]
    if "theme_styling" in value:
        import aws_sdk_appstream.types.theme_styling

        out["ThemeStyling"] = (
            aws_sdk_appstream.types.theme_styling.serialize_aws_json_1_1(
                value["theme_styling"]
            )
        )
    if "organization_logo_s3_location" in value:
        import aws_sdk_appstream.types.s3_location

        out["OrganizationLogoS3Location"] = (
            aws_sdk_appstream.types.s3_location.serialize_aws_json_1_1(
                value["organization_logo_s3_location"]
            )
        )
    if "favicon_s3_location" in value:
        import aws_sdk_appstream.types.s3_location

        out["FaviconS3Location"] = (
            aws_sdk_appstream.types.s3_location.serialize_aws_json_1_1(
                value["favicon_s3_location"]
            )
        )
    if "state" in value:
        import aws_sdk_appstream.types.theme_state

        out["State"] = aws_sdk_appstream.types.theme_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "attributes_to_delete" in value:
        import aws_sdk_appstream.types.theme_attributes

        out["AttributesToDelete"] = (
            aws_sdk_appstream.types.theme_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateThemeForStackRequest:
    out: UpdateThemeForStackRequest = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "FooterLinks" in data:
        import aws_sdk_appstream.types.theme_footer_links

        out["footer_links"] = (
            aws_sdk_appstream.types.theme_footer_links.deserialize_aws_json_1_1(
                data["FooterLinks"]
            )
        )
    if "TitleText" in data:
        out["title_text"] = data["TitleText"]
    if "ThemeStyling" in data:
        import aws_sdk_appstream.types.theme_styling

        out["theme_styling"] = (
            aws_sdk_appstream.types.theme_styling.deserialize_aws_json_1_1(
                data["ThemeStyling"]
            )
        )
    if "OrganizationLogoS3Location" in data:
        import aws_sdk_appstream.types.s3_location

        out["organization_logo_s3_location"] = (
            aws_sdk_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["OrganizationLogoS3Location"]
            )
        )
    if "FaviconS3Location" in data:
        import aws_sdk_appstream.types.s3_location

        out["favicon_s3_location"] = (
            aws_sdk_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["FaviconS3Location"]
            )
        )
    if "State" in data:
        import aws_sdk_appstream.types.theme_state

        out["state"] = aws_sdk_appstream.types.theme_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "AttributesToDelete" in data:
        import aws_sdk_appstream.types.theme_attributes

        out["attributes_to_delete"] = (
            aws_sdk_appstream.types.theme_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    return out

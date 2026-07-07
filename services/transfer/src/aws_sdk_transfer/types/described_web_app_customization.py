"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebAppCustomization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.web_app_favicon_file
    import aws_sdk_transfer.types.web_app_id
    import aws_sdk_transfer.types.web_app_logo_file
    import aws_sdk_transfer.types.web_app_title


class DescribedWebAppCustomization(TypedDict, closed=True):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>Returns the Amazon Resource Name (ARN) for the web app.</p>"""
    web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId"
    """<p>Returns the unique identifier for your web app.</p>"""
    title: NotRequired["aws_sdk_transfer.types.web_app_title.WebAppTitle"]
    """<p>Returns the page title that you defined for your web app.</p>"""
    logo_file: NotRequired["aws_sdk_transfer.types.web_app_logo_file.WebAppLogoFile"]
    """<p>Returns a logo file data string (in base64 encoding).</p>"""
    favicon_file: NotRequired[
        "aws_sdk_transfer.types.web_app_favicon_file.WebAppFaviconFile"
    ]
    """<p>Returns an icon file data string (in base64 encoding).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebAppCustomization) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["WebAppId"] = value["web_app_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "logo_file" in value:
        import aws_sdk_transfer.types.web_app_logo_file

        out["LogoFile"] = (
            aws_sdk_transfer.types.web_app_logo_file.serialize_aws_json_1_1(
                value["logo_file"]
            )
        )
    if "favicon_file" in value:
        import aws_sdk_transfer.types.web_app_favicon_file

        out["FaviconFile"] = (
            aws_sdk_transfer.types.web_app_favicon_file.serialize_aws_json_1_1(
                value["favicon_file"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedWebAppCustomization:
    out: DescribedWebAppCustomization = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedWebAppCustomization.arn required")
    if "WebAppId" in data:
        out["web_app_id"] = data["WebAppId"]
    else:
        raise DeserializationError("DescribedWebAppCustomization.web_app_id required")
    if "Title" in data:
        out["title"] = data["Title"]
    if "LogoFile" in data:
        import aws_sdk_transfer.types.web_app_logo_file

        out["logo_file"] = (
            aws_sdk_transfer.types.web_app_logo_file.deserialize_aws_json_1_1(
                data["LogoFile"]
            )
        )
    if "FaviconFile" in data:
        import aws_sdk_transfer.types.web_app_favicon_file

        out["favicon_file"] = (
            aws_sdk_transfer.types.web_app_favicon_file.deserialize_aws_json_1_1(
                data["FaviconFile"]
            )
        )
    return out

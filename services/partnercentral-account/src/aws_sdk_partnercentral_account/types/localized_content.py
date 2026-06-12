"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#LocalizedContent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.locale
    import aws_sdk_partnercentral_account.types.unicode_string
    import aws_sdk_partnercentral_account.types.url


class LocalizedContent(TypedDict):
    display_name: "aws_sdk_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The localized display name for the partner.</p>"""
    description: "aws_sdk_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The localized description of the partner's business and services.</p>"""
    website_url: "aws_sdk_partnercentral_account.types.url.Url"
    """<p>The localized website URL for the partner.</p>"""
    logo_url: "aws_sdk_partnercentral_account.types.url.Url"
    """<p>The URL to the partner's logo image for this locale.</p>"""
    locale: "aws_sdk_partnercentral_account.types.locale.Locale"
    """<p>The locale or language code for the localized content.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LocalizedContent) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    out["Description"] = value["description"]
    out["WebsiteUrl"] = value["website_url"]
    out["LogoUrl"] = value["logo_url"]
    out["Locale"] = value["locale"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LocalizedContent:
    out: LocalizedContent = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("LocalizedContent.display_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("LocalizedContent.description required")
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    else:
        raise DeserializationError("LocalizedContent.website_url required")
    if "LogoUrl" in data:
        out["logo_url"] = data["LogoUrl"]
    else:
        raise DeserializationError("LocalizedContent.logo_url required")
    if "Locale" in data:
        out["locale"] = data["Locale"]
    else:
        raise DeserializationError("LocalizedContent.locale required")
    return out

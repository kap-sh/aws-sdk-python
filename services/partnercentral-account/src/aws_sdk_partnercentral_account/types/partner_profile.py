"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.industry_segment_list
    import aws_sdk_partnercentral_account.types.locale
    import aws_sdk_partnercentral_account.types.localized_content_list
    import aws_sdk_partnercentral_account.types.partner_profile_id
    import aws_sdk_partnercentral_account.types.primary_solution_type
    import aws_sdk_partnercentral_account.types.unicode_string
    import aws_sdk_partnercentral_account.types.url


class PartnerProfile(TypedDict, closed=True):
    display_name: "aws_sdk_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The public display name for the partner organization.</p>"""
    description: "aws_sdk_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>A description of the partner's business, services, and capabilities.</p>"""
    website_url: "aws_sdk_partnercentral_account.types.url.Url"
    """<p>The partner's primary website URL.</p>"""
    logo_url: "aws_sdk_partnercentral_account.types.url.Url"
    """<p>The URL to the partner's logo image.</p>"""
    primary_solution_type: (
        "aws_sdk_partnercentral_account.types.primary_solution_type.PrimarySolutionType"
    )
    """<p>The primary type of solution or service the partner provides.</p>"""
    industry_segments: (
        "aws_sdk_partnercentral_account.types.industry_segment_list.IndustrySegmentList"
    )
    """<p>The industry segments or verticals that the partner serves.</p>"""
    translation_source_locale: "aws_sdk_partnercentral_account.types.locale.Locale"
    """<p>The source locale used for automatic translation of profile content.</p>"""
    localized_contents: NotRequired[
        "aws_sdk_partnercentral_account.types.localized_content_list.LocalizedContentList"
    ]
    """<p>A list of localized content versions for different languages and regions.</p>"""
    profile_id: NotRequired[
        "aws_sdk_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    ]
    """<p>The unique identifier of the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerProfile) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    out["Description"] = value["description"]
    out["WebsiteUrl"] = value["website_url"]
    out["LogoUrl"] = value["logo_url"]
    import aws_sdk_partnercentral_account.types.primary_solution_type

    out["PrimarySolutionType"] = (
        aws_sdk_partnercentral_account.types.primary_solution_type.serialize_aws_json_1_0(
            value["primary_solution_type"]
        )
    )
    import aws_sdk_partnercentral_account.types.industry_segment_list

    out["IndustrySegments"] = (
        aws_sdk_partnercentral_account.types.industry_segment_list.serialize_aws_json_1_0(
            value["industry_segments"]
        )
    )
    out["TranslationSourceLocale"] = value["translation_source_locale"]
    if "localized_contents" in value:
        import aws_sdk_partnercentral_account.types.localized_content_list

        out["LocalizedContents"] = (
            aws_sdk_partnercentral_account.types.localized_content_list.serialize_aws_json_1_0(
                value["localized_contents"]
            )
        )
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnerProfile:
    out: PartnerProfile = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("PartnerProfile.display_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("PartnerProfile.description required")
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    else:
        raise DeserializationError("PartnerProfile.website_url required")
    if "LogoUrl" in data:
        out["logo_url"] = data["LogoUrl"]
    else:
        raise DeserializationError("PartnerProfile.logo_url required")
    if "PrimarySolutionType" in data:
        import aws_sdk_partnercentral_account.types.primary_solution_type

        out["primary_solution_type"] = (
            aws_sdk_partnercentral_account.types.primary_solution_type.deserialize_aws_json_1_0(
                data["PrimarySolutionType"]
            )
        )
    else:
        raise DeserializationError("PartnerProfile.primary_solution_type required")
    if "IndustrySegments" in data:
        import aws_sdk_partnercentral_account.types.industry_segment_list

        out["industry_segments"] = (
            aws_sdk_partnercentral_account.types.industry_segment_list.deserialize_aws_json_1_0(
                data["IndustrySegments"]
            )
        )
    else:
        raise DeserializationError("PartnerProfile.industry_segments required")
    if "TranslationSourceLocale" in data:
        out["translation_source_locale"] = data["TranslationSourceLocale"]
    else:
        raise DeserializationError("PartnerProfile.translation_source_locale required")
    if "LocalizedContents" in data:
        import aws_sdk_partnercentral_account.types.localized_content_list

        out["localized_contents"] = (
            aws_sdk_partnercentral_account.types.localized_content_list.deserialize_aws_json_1_0(
                data["LocalizedContents"]
            )
        )
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    return out

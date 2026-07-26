"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#TaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.industry_segment_list
    import capo_partnercentral_account.types.locale
    import capo_partnercentral_account.types.localized_content_list
    import capo_partnercentral_account.types.primary_solution_type
    import capo_partnercentral_account.types.unicode_string
    import capo_partnercentral_account.types.url


class TaskDetails(TypedDict, closed=True):
    display_name: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The updated display name for the partner profile.</p>"""
    description: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The updated description for the partner profile.</p>"""
    website_url: "capo_partnercentral_account.types.url.Url"
    """<p>The updated website URL for the partner profile.</p>"""
    logo_url: "capo_partnercentral_account.types.url.Url"
    """<p>The updated logo URL for the partner profile.</p>"""
    primary_solution_type: (
        "capo_partnercentral_account.types.primary_solution_type.PrimarySolutionType"
    )
    """<p>The updated primary solution type for the partner profile.</p>"""
    industry_segments: (
        "capo_partnercentral_account.types.industry_segment_list.IndustrySegmentList"
    )
    """<p>The updated industry segments for the partner profile.</p>"""
    translation_source_locale: "capo_partnercentral_account.types.locale.Locale"
    """<p>The updated translation source locale for the partner profile.</p>"""
    localized_contents: NotRequired[
        "capo_partnercentral_account.types.localized_content_list.LocalizedContentList"
    ]
    """<p>The updated localized content for the partner profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskDetails) -> dict:
    out: dict = {}
    out["DisplayName"] = value["display_name"]
    out["Description"] = value["description"]
    out["WebsiteUrl"] = value["website_url"]
    out["LogoUrl"] = value["logo_url"]
    import capo_partnercentral_account.types.primary_solution_type

    out["PrimarySolutionType"] = (
        capo_partnercentral_account.types.primary_solution_type.serialize_aws_json_1_0(
            value["primary_solution_type"]
        )
    )
    import capo_partnercentral_account.types.industry_segment_list

    out["IndustrySegments"] = (
        capo_partnercentral_account.types.industry_segment_list.serialize_aws_json_1_0(
            value["industry_segments"]
        )
    )
    out["TranslationSourceLocale"] = value["translation_source_locale"]
    if "localized_contents" in value:
        import capo_partnercentral_account.types.localized_content_list

        out["LocalizedContents"] = (
            capo_partnercentral_account.types.localized_content_list.serialize_aws_json_1_0(
                value["localized_contents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskDetails:
    out: TaskDetails = {}  # type: ignore[typeddict-item]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    else:
        raise DeserializationError("TaskDetails.display_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("TaskDetails.description required")
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    else:
        raise DeserializationError("TaskDetails.website_url required")
    if "LogoUrl" in data:
        out["logo_url"] = data["LogoUrl"]
    else:
        raise DeserializationError("TaskDetails.logo_url required")
    if "PrimarySolutionType" in data:
        import capo_partnercentral_account.types.primary_solution_type

        out["primary_solution_type"] = (
            capo_partnercentral_account.types.primary_solution_type.deserialize_aws_json_1_0(
                data["PrimarySolutionType"]
            )
        )
    else:
        raise DeserializationError("TaskDetails.primary_solution_type required")
    if "IndustrySegments" in data:
        import capo_partnercentral_account.types.industry_segment_list

        out["industry_segments"] = (
            capo_partnercentral_account.types.industry_segment_list.deserialize_aws_json_1_0(
                data["IndustrySegments"]
            )
        )
    else:
        raise DeserializationError("TaskDetails.industry_segments required")
    if "TranslationSourceLocale" in data:
        out["translation_source_locale"] = data["TranslationSourceLocale"]
    else:
        raise DeserializationError("TaskDetails.translation_source_locale required")
    if "LocalizedContents" in data:
        import capo_partnercentral_account.types.localized_content_list

        out["localized_contents"] = (
            capo_partnercentral_account.types.localized_content_list.deserialize_aws_json_1_0(
                data["LocalizedContents"]
            )
        )
    return out

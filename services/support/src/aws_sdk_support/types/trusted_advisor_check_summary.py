"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.boolean
    import aws_sdk_support.types.string
    import aws_sdk_support.types.trusted_advisor_category_specific_summary
    import aws_sdk_support.types.trusted_advisor_resources_summary


class TrustedAdvisorCheckSummary(TypedDict):
    check_id: "aws_sdk_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check.</p>"""
    timestamp: "aws_sdk_support.types.string.String"
    """<p>The time of the last refresh of the check.</p>"""
    status: "aws_sdk_support.types.string.String"
    """<p>The alert status of the check: \"ok\" (green), \"warning\" (yellow), \"error\" (red), or \"not_available\".</p>"""
    has_flagged_resources: "aws_sdk_support.types.boolean.Boolean"
    """<p>Specifies whether the Trusted Advisor check has flagged resources.</p>"""
    resources_summary: "aws_sdk_support.types.trusted_advisor_resources_summary.TrustedAdvisorResourcesSummary"
    category_specific_summary: "aws_sdk_support.types.trusted_advisor_category_specific_summary.TrustedAdvisorCategorySpecificSummary"
    """<p>Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckSummary) -> dict:
    out: dict = {}
    out["checkId"] = value["check_id"]
    out["timestamp"] = value["timestamp"]
    out["status"] = value["status"]
    out["hasFlaggedResources"] = value.get("has_flagged_resources", False)
    import aws_sdk_support.types.trusted_advisor_resources_summary

    out["resourcesSummary"] = (
        aws_sdk_support.types.trusted_advisor_resources_summary.serialize_aws_json_1_1(
            value["resources_summary"]
        )
    )
    import aws_sdk_support.types.trusted_advisor_category_specific_summary

    out["categorySpecificSummary"] = (
        aws_sdk_support.types.trusted_advisor_category_specific_summary.serialize_aws_json_1_1(
            value["category_specific_summary"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCheckSummary:
    out: TrustedAdvisorCheckSummary = {}  # type: ignore[typeddict-item]
    if "checkId" in data:
        out["check_id"] = data["checkId"]
    else:
        raise DeserializationError("TrustedAdvisorCheckSummary.check_id required")
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    else:
        raise DeserializationError("TrustedAdvisorCheckSummary.timestamp required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("TrustedAdvisorCheckSummary.status required")
    if "hasFlaggedResources" in data:
        out["has_flagged_resources"] = data["hasFlaggedResources"]
    else:
        out["has_flagged_resources"] = False
    if "resourcesSummary" in data:
        import aws_sdk_support.types.trusted_advisor_resources_summary

        out["resources_summary"] = (
            aws_sdk_support.types.trusted_advisor_resources_summary.deserialize_aws_json_1_1(
                data["resourcesSummary"]
            )
        )
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckSummary.resources_summary required"
        )
    if "categorySpecificSummary" in data:
        import aws_sdk_support.types.trusted_advisor_category_specific_summary

        out["category_specific_summary"] = (
            aws_sdk_support.types.trusted_advisor_category_specific_summary.deserialize_aws_json_1_1(
                data["categorySpecificSummary"]
            )
        )
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckSummary.category_specific_summary required"
        )
    return out

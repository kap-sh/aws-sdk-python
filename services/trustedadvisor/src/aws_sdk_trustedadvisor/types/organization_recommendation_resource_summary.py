"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#OrganizationRecommendationResourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_trustedadvisor.types.account_id
    import aws_sdk_trustedadvisor.types.exclusion_status
    import aws_sdk_trustedadvisor.types.organization_recommendation_arn
    import aws_sdk_trustedadvisor.types.recommendation_region_code
    import aws_sdk_trustedadvisor.types.recommendation_resource_arn
    import aws_sdk_trustedadvisor.types.resource_status
    import aws_sdk_trustedadvisor.types.string_map


class OrganizationRecommendationResourceSummary(TypedDict):
    id: "str"
    """<p>The ID of the Recommendation Resource</p>"""
    arn: "aws_sdk_trustedadvisor.types.recommendation_resource_arn.RecommendationResourceArn"
    """<p>The ARN of the Recommendation Resource</p>"""
    aws_resource_id: "str"
    """<p>The AWS resource identifier. There are certain checks that generate recommendation resources without an awsResourceId.</p>"""
    region_code: "aws_sdk_trustedadvisor.types.recommendation_region_code.RecommendationRegionCode"
    """<p>The AWS Region code that the Recommendation Resource is in</p>"""
    status: "aws_sdk_trustedadvisor.types.resource_status.ResourceStatus"
    """<p>The current status of the Recommendation Resource</p>"""
    metadata: "aws_sdk_trustedadvisor.types.string_map.StringMap"
    """<p>Metadata associated with the Recommendation Resource</p>"""
    last_updated_at: "datetime.datetime"
    """<p>When the Recommendation Resource was last updated</p>"""
    exclusion_status: "aws_sdk_trustedadvisor.types.exclusion_status.ExclusionStatus"
    """<p>The exclusion status of the Recommendation Resource</p>"""
    account_id: NotRequired["aws_sdk_trustedadvisor.types.account_id.AccountId"]
    """<p>The AWS account ID</p>"""
    recommendation_arn: "aws_sdk_trustedadvisor.types.organization_recommendation_arn.OrganizationRecommendationArn"
    """<p>The Recommendation ARN</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationRecommendationResourceSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["awsResourceId"] = value["aws_resource_id"]
    out["regionCode"] = value["region_code"]
    import aws_sdk_trustedadvisor.types.resource_status

    out["status"] = aws_sdk_trustedadvisor.types.resource_status.serialize_json(
        value["status"]
    )
    import aws_sdk_trustedadvisor.types.string_map

    out["metadata"] = aws_sdk_trustedadvisor.types.string_map.serialize_json(
        value["metadata"]
    )
    import aws_sdk_trustedadvisor.types._prelude.timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_trustedadvisor.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import aws_sdk_trustedadvisor.types.exclusion_status

    out["exclusionStatus"] = (
        aws_sdk_trustedadvisor.types.exclusion_status.serialize_json(
            value.get("exclusion_status", "included")
        )
    )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    out["recommendationArn"] = value["recommendation_arn"]
    return out


def deserialize_json(data: dict) -> OrganizationRecommendationResourceSummary:
    out: OrganizationRecommendationResourceSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.arn required"
        )
    if "awsResourceId" in data:
        out["aws_resource_id"] = data["awsResourceId"]
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.aws_resource_id required"
        )
    if "regionCode" in data:
        out["region_code"] = data["regionCode"]
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.region_code required"
        )
    if "status" in data:
        import aws_sdk_trustedadvisor.types.resource_status

        out["status"] = aws_sdk_trustedadvisor.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.status required"
        )
    if "metadata" in data:
        import aws_sdk_trustedadvisor.types.string_map

        out["metadata"] = aws_sdk_trustedadvisor.types.string_map.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.metadata required"
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_trustedadvisor.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_trustedadvisor.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.last_updated_at required"
        )
    if "exclusionStatus" in data:
        import aws_sdk_trustedadvisor.types.exclusion_status

        out["exclusion_status"] = (
            aws_sdk_trustedadvisor.types.exclusion_status.deserialize_json(
                data["exclusionStatus"]
            )
        )
    else:
        out["exclusion_status"] = "included"
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "recommendationArn" in data:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        raise DeserializationError(
            "OrganizationRecommendationResourceSummary.recommendation_arn required"
        )
    return out

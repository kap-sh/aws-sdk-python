"""Generated from Smithy shape ``com.amazonaws.securityhub#GetRecommendedPolicyV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.recommendation_error
    import aws_sdk_securityhub.types.recommendation_status
    import aws_sdk_securityhub.types.recommendation_steps
    import aws_sdk_securityhub.types.recommendation_type


class GetRecommendedPolicyV2Response(TypedDict):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""
    recommendation_type: NotRequired[
        "aws_sdk_securityhub.types.recommendation_type.RecommendationType"
    ]
    """<p>The type of recommendation for the finding.</p>"""
    recommendation_steps: NotRequired[
        "aws_sdk_securityhub.types.recommendation_steps.RecommendationSteps"
    ]
    """<p>The recommended steps to take to resolve the finding.</p>"""
    error: NotRequired[
        "aws_sdk_securityhub.types.recommendation_error.RecommendationError"
    ]
    """<p>Detailed information for a <code>FAILED</code> retrieval status.</p>"""
    status: NotRequired[
        "aws_sdk_securityhub.types.recommendation_status.RecommendationStatus"
    ]
    """<p>The current status of the recommended policy retrieval.</p>"""
    resource_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the resource of the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendedPolicyV2Response) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommendation_type" in value:
        import aws_sdk_securityhub.types.recommendation_type

        out["RecommendationType"] = (
            aws_sdk_securityhub.types.recommendation_type.serialize_json(
                value["recommendation_type"]
            )
        )
    if "recommendation_steps" in value:
        import aws_sdk_securityhub.types.recommendation_steps

        out["RecommendationSteps"] = (
            aws_sdk_securityhub.types.recommendation_steps.serialize_json(
                value["recommendation_steps"]
            )
        )
    if "error" in value:
        import aws_sdk_securityhub.types.recommendation_error

        out["Error"] = aws_sdk_securityhub.types.recommendation_error.serialize_json(
            value["error"]
        )
    if "status" in value:
        import aws_sdk_securityhub.types.recommendation_status

        out["Status"] = aws_sdk_securityhub.types.recommendation_status.serialize_json(
            value["status"]
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> GetRecommendedPolicyV2Response:
    out: GetRecommendedPolicyV2Response = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecommendationType" in data:
        import aws_sdk_securityhub.types.recommendation_type

        out["recommendation_type"] = (
            aws_sdk_securityhub.types.recommendation_type.deserialize_json(
                data["RecommendationType"]
            )
        )
    if "RecommendationSteps" in data:
        import aws_sdk_securityhub.types.recommendation_steps

        out["recommendation_steps"] = (
            aws_sdk_securityhub.types.recommendation_steps.deserialize_json(
                data["RecommendationSteps"]
            )
        )
    if "Error" in data:
        import aws_sdk_securityhub.types.recommendation_error

        out["error"] = aws_sdk_securityhub.types.recommendation_error.deserialize_json(
            data["Error"]
        )
    if "Status" in data:
        import aws_sdk_securityhub.types.recommendation_status

        out["status"] = (
            aws_sdk_securityhub.types.recommendation_status.deserialize_json(
                data["Status"]
            )
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out

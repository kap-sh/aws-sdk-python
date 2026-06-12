"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetArchitectureRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.max_results


class GetArchitectureRecommendationsRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    recovery_group_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>The name of a recovery group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArchitectureRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetArchitectureRecommendationsRequest:
    out: GetArchitectureRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.max_results


class ListRulesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    resource_type: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The resource type that a readiness rule applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRulesRequest:
    out: ListRulesRequest = {}  # type: ignore[typeddict-item]
    return out

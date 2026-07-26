"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetReadinessCheckResourceStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.max_results


class GetReadinessCheckResourceStatusRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_route53_recovery_readiness.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a readiness check.</p>"""
    resource_identifier: "capo_route53_recovery_readiness.types.__string.__string"
    """<p>The resource identifier, which is the Amazon Resource Name (ARN) or the identifier generated for the resource by Application Recovery Controller (for example, for a DNS target resource).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadinessCheckResourceStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadinessCheckResourceStatusRequest:
    out: GetReadinessCheckResourceStatusRequest = {}  # type: ignore[typeddict-item]
    return out
